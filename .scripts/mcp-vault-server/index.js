const { Server } = require("@modelcontextprotocol/sdk/server/index.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
} = require("@modelcontextprotocol/sdk/types.js");
const fs = require("fs");
const path = require("path");

const VAULT_ROOT = path.resolve(__dirname, "..", "..");

const server = new Server(
  {
    name: "will-obsidian-mcp",
    version: "2.0.0",
  },
  {
    capabilities: {
      resources: {},
      tools: {},
    },
  }
);

// Helper: validate path safety
function safePath(relativePath) {
  const fullPath = path.resolve(VAULT_ROOT, relativePath);
  if (!fullPath.startsWith(VAULT_ROOT)) {
    throw new Error("Acesso negado: caminho fora do vault");
  }
  return fullPath;
}

// Helper: extract frontmatter tags
function extractTags(content) {
  const tags = [];
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (match) {
    const frontmatter = match[1];
    const tagMatch = frontmatter.match(/tags:\s*\[([^\]]*)\]/);
    if (tagMatch) {
      tagMatch[1].split(",").forEach(t => tags.push(t.trim()));
    }
    const tagListMatch = frontmatter.match(/tags:\n((?:\s+-\s+.*\n)*)/);
    if (tagListMatch) {
      tagListMatch[1].split("\n").forEach(line => {
        const t = line.match(/\s*-\s*(.+)/);
        if (t) tags.push(t[1].trim());
      });
    }
  }
  return tags;
}

// Helper: extract wiki links from content
function extractWikiLinks(content) {
  const links = [];
  const regex = /\[\[([^\]|]+)(?:\|[^\]]*)?\]\]/g;
  let m;
  while ((m = regex.exec(content)) !== null) {
    links.push(m[1].trim());
  }
  return [...new Set(links)];
}

// Helper: find backlinks for a given file
function findBacklinks(targetPath) {
  const targetName = path.basename(targetPath, ".md");
  const backlinks = [];
  const walkDir = (dir) => {
    try {
      const entries = fs.readdirSync(dir, { withFileTypes: true });
      for (const entry of entries) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) {
          if (entry.name !== ".git" && entry.name !== ".obsidian" && entry.name !== "node_modules" && entry.name !== "__pycache__") {
            walkDir(full);
          }
        } else if (entry.name.endsWith(".md")) {
          const content = fs.readFileSync(full, "utf-8");
          const linkPattern = new RegExp(`\\[\\[${escapeRegex(targetName)}(\\|[^\\]]*)?\\]\\]`);
          if (linkPattern.test(content)) {
            backlinks.push(path.relative(VAULT_ROOT, full));
          }
        }
      }
    } catch (err) {
      // Ignore directories we can't read
    }
  };
  walkDir(VAULT_ROOT);
  return backlinks;
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

// Helper: get all markdown files
function getAllMarkdownFiles() {
  const files = [];
  const walkDir = (dir) => {
    try {
      const entries = fs.readdirSync(dir, { withFileTypes: true });
      for (const entry of entries) {
        const full = path.join(dir, entry.name);
        if (entry.isDirectory()) {
          if (entry.name !== ".git" && entry.name !== ".obsidian" && entry.name !== "node_modules" && entry.name !== "__pycache__") {
            walkDir(full);
          }
        } else if (entry.name.endsWith(".md")) {
          files.push(full);
        }
      }
    } catch (err) {
      // Ignore directories we can't read
    }
  };
  walkDir(VAULT_ROOT);
  return files;
}

// Tools definition
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "read_vault_file",
        description: "Lê o conteúdo de um arquivo Markdown no vault do Obsidian",
        inputSchema: {
          type: "object",
          properties: {
            relativePath: {
              type: "string",
              description: "Caminho relativo ao root do vault (ex: 'Projetos/Projetos.md')",
            },
          },
          required: ["relativePath"],
        },
      },
      {
        name: "write_vault_file",
        description: "Escreve conteúdo em um arquivo Markdown no vault do Obsidian",
        inputSchema: {
          type: "object",
          properties: {
            relativePath: {
              type: "string",
              description: "Caminho relativo ao root do vault (ex: 'Projetos/Novo-Arquivo.md')",
            },
            content: {
              type: "string",
              description: "Conteúdo Markdown para escrever no arquivo",
            },
            overwrite: {
              type: "boolean",
              description: "Se verdadeiro, sobrescreve o arquivo se existir (padrão: false)",
              default: false,
            },
          },
          required: ["relativePath", "content"],
        },
      },
      {
        name: "list_vault_files",
        description: "Lista arquivos no vault para entender a estrutura",
        inputSchema: {
          type: "object",
          properties: {
            subFolder: {
              type: "string",
              description: "Pasta opcional para listar (ex: 'JARVIS')",
            },
          },
        },
      },
      {
        name: "search_vault",
        description: "Busca por um termo em todos os arquivos Markdown do vault",
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "Termo de busca",
            },
          },
          required: ["query"],
        },
      },
      {
        name: "vault_graph_query",
        description: "Consulta o grafo de conhecimento: lista backlinks e links saíntes de um arquivo",
        inputSchema: {
          type: "object",
          properties: {
            relativePath: {
              type: "string",
              description: "Caminho relativo do arquivo para analisar (ex: 'Conhecimento-Geral/Filosofia/ETICA.md')",
            },
          },
          required: ["relativePath"],
        },
      },
      {
        name: "vault_search_regex",
        description: "Busca avançada usando expressões regulares em todos os arquivos Markdown do vault",
        inputSchema: {
          type: "object",
          properties: {
            pattern: {
              type: "string",
              description: "Padrão de expressão regular para busca",
            },
            flags: {
              type: "string",
              description: "Flags da regex (ex: 'i' para case-insensitive, 'g' para global)",
              default: "",
            },
          },
          required: ["pattern"],
        },
      },
      {
        name: "vault_tag_taxonomy",
        description: "Lista todas as tags utilizadas no vault com contagem e exemplos",
        inputSchema: {
          type: "object",
          properties: {
            limit: {
              type: "integer",
              description: "Limite de tags a retornar (padrão: 100)",
              default: 100,
            },
            sortBy: {
              type: "string",
              description: "Ordenar por: 'count' (contagem) ou 'name' (nome alfabético)",
              default: "count",
            },
          },
        },
      },
      {
        name: "vault_stats",
        description: "Retorna estatísticas gerais do vault: contagem de arquivos, linhas, tags, etc.",
        inputSchema: {
          type: "object",
          properties: {},
        },
      },
    ],
  };
});

// Tool handlers
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "read_vault_file": {
      const filePath = safePath(args.relativePath);
      if (!fs.existsSync(filePath)) throw new Error("Arquivo não encontrado");
      
      const content = fs.readFileSync(filePath, "utf-8");
      return {
        content: [{ type: "text", text: content }],
      };
    }

    case "write_vault_file": {
      const filePath = safePath(args.relativePath);
      
      // Create parent directories if they don't exist
      const dir = path.dirname(filePath);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      
      // Check if file exists and overwrite flag
      if (fs.existsSync(filePath) && !args.overwrite) {
        throw new Error("Arquivo já existe. Use overwrite:true para substituir.");
      }
      
      fs.writeFileSync(filePath, args.content, "utf-8");
      
      return {
        content: [{ 
          type: "text", 
          text: `Arquivo escrito com sucesso: ${args.relativePath}\nTamanho: ${Buffer.byteLength(args.content, 'utf-8')} bytes` 
        }],
      };
    }

    case "list_vault_files": {
      const targetDir = args.subFolder 
        ? safePath(args.subFolder) 
        : VAULT_ROOT;
      
      if (!fs.existsSync(targetDir)) throw new Error("Diretório não encontrado");
      
      const files = [];
      const walkDir = (dir) => {
        try {
          const entries = fs.readdirSync(dir, { withFileTypes: true });
          for (const entry of entries) {
            const full = path.join(dir, entry.name);
            if (entry.isDirectory()) {
              if (entry.name !== ".git" && entry.name !== ".obsidian" && entry.name !== "node_modules" && entry.name !== "__pycache__") {
                walkDir(full);
              }
            } else {
              files.push(path.relative(VAULT_ROOT, full));
            }
          }
        } catch (err) {
          // Ignore directories we can't read
        }
      };
      walkDir(targetDir);
      
      return {
        content: [{ type: "text", text: files.join("\n") }],
      };
    }

    case "search_vault": {
      const query = args.query.toLowerCase();
      const results = [];
      const getAllFiles = (dir) => {
          const files = fs.readdirSync(dir);
          files.forEach(file => {
              const fullPath = path.join(dir, file);
              try {
                const stat = fs.statSync(fullPath);
                if (stat.isDirectory()) {
                  if (file !== ".git" && file !== ".obsidian" && file !== "node_modules" && file !== "__pycache__") {
                    getAllFiles(fullPath);
                  }
                } else if (file.endsWith(".md")) {
                  const content = fs.readFileSync(fullPath, "utf-8");
                  if (content.toLowerCase().includes(query)) {
                    results.push(path.relative(VAULT_ROOT, fullPath));
                  }
                }
              } catch (err) {
                // Ignore files we can't read
              }
          });
      };
      getAllFiles(VAULT_ROOT);
      return {
        content: [{ type: "text", text: `Resultados encontrados em:\n${results.join("\n")}` }],
      };
    }

    case "vault_graph_query": {
      const filePath = safePath(args.relativePath);
      if (!fs.existsSync(filePath)) throw new Error("Arquivo não encontrado");
      
      const content = fs.readFileSync(filePath, "utf-8");
      const outgoingLinks = extractWikiLinks(content);
      const backlinks = findBacklinks(filePath);
      
      return {
        content: [{ 
          type: "text", 
          text: `Análise de grafo para: ${args.relativePath}\n\n` +
                `Links saíntes (${outgoingLinks.length}):\n${outgoingLinks.map(l => `  - [[${l}}]`).join("\n") || "  Nenhum"}\n\n` +
                `Backlinks (${backlinks.length}):\n${backlinks.map(b => `  - [[${b}}]`).join("\n") || "  Nenhum"}`
        }],
      };
    }

    case "vault_search_regex": {
      let regex;
      try {
        regex = new RegExp(args.pattern, args.flags);
      } catch (err) {
        throw new Error(`Expressão regular inválida: ${err.message}`);
      }
      
      const results = [];
      const getAllFiles = (dir) => {
          const files = fs.readdirSync(dir);
          files.forEach(file => {
              const fullPath = path.join(dir, file);
              try {
                const stat = fs.statSync(fullPath);
                if (stat.isDirectory()) {
                  if (file !== ".git" && file !== ".obsidian" && file !== "node_modules" && file !== "__pycache__") {
                    getAllFiles(fullPath);
                  }
                } else if (file.endsWith(".md")) {
                  const content = fs.readFileSync(fullPath, "utf-8");
                  const matches = content.match(regex);
                  if (matches) {
                    results.push({
                      file: path.relative(VAULT_ROOT, fullPath),
                      matches: matches
                    });
                  }
                }
              } catch (err) {
                // Ignore files we can't read
              }
          });
      };
      getAllFiles(VAULT_ROOT);
      
      const output = results.map(r => {
        const preview = r.matches.slice(0, 3).map(m => `"${m.trim()}"`).join(", ");
        const more = r.matches.length > 3 ? ` e mais ${r.matches.length - 3}...` : "";
        return `- [[${r.file}]]${more} (${preview})`;
      }).join("\n");
      
      return {
        content: [{ 
          type: "text", 
          text: `Busca regex: /${args.pattern}/${args.flags}\n\n${results.length} arquivos com matches:\n\n${output || "Nenhum match encontrado."}`
        }],
      };
    }

    case "vault_tag_taxonomy": {
      const tagCounts = new Map();
      const tagExamples = new Map();
      
      const files = getAllMarkdownFiles();
      files.forEach(filePath => {
        try {
          const content = fs.readFileSync(filePath, "utf-8");
          const tags = extractTags(content);
          const relativePath = path.relative(VAULT_ROOT, filePath);
          
          tags.forEach(tag => {
            const count = tagCounts.get(tag) || 0;
            tagCounts.set(tag, count + 1);
            
            const examples = tagExamples.get(tag) || [];
            if (examples.length < 3) {
              examples.push(relativePath);
              tagExamples.set(tag, examples);
            }
          });
        } catch (err) {
          // Ignore files we can't read
        }
      });
      
      // Convert to array and sort
      const tagsArray = Array.from(tagCounts.entries()).map(([tag, count]) => ({
        tag,
        count,
        examples: tagExamples.get(tag) || []
      }));
      
      if (args.sortBy === "name") {
        tagsArray.sort((a, b) => a.tag.localeCompare(b.tag));
      } else {
        // Default sort by count (descending)
        tagsArray.sort((a, b) => b.count - a.count);
      }
      
      // Apply limit
      const limitedTags = args.limit ? tagsArray.slice(0, args.limit) : tagsArray;
      
      const output = limitedTags.map(t => {
        const examplesStr = t.examples.slice(0, 2).map(e => `[[${e}}]`).join(", ");
        const more = t.examples.length > 2 ? ` +${t.examples.length - 2} mais` : "";
        return `- **${t.tag}** (${t.count} usos): ${examplesStr}${more}`;
      }).join("\n");
      
      return {
        content: [{ 
          type: "text", 
          text: `Taxonomia de Tags no Vault\n\nTotal de tags únicas: ${tagCounts.size}\n\n${output || "Nenhuma tag encontrada."}`
        }],
      };
    }

    case "vault_stats": {
      const files = getAllMarkdownFiles();
      
      let totalLines = 0;
      let totalSize = 0;
      const tagCounts = new Map();
      
      files.forEach(filePath => {
        try {
          const content = fs.readFileSync(filePath, "utf-8");
          const lines = content.split('\n').length;
          const size = Buffer.byteLength(content, 'utf-8');
          
          totalLines += lines;
          totalSize += size;
          
          // Count tags
          const tags = extractTags(content);
          tags.forEach(tag => {
            const count = tagCounts.get(tag) || 0;
            tagCounts.set(tag, count + 1);
          });
        } catch (err) {
          // Ignore files we can't read
        }
      });
      
      const topTags = Array.from(tagCounts.entries())
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10)
        .map(([tag, count]) => `${tag}: ${count}`)
        .join(", ");
      
      return {
        content: [{ 
          type: "text", 
          text: `Estatísticas do Vault Obsidian\n\n` +
                `Arquivos Markdown: ${files.length}\n` +
                `Linhas totais: ${totalLines.toLocaleString()}\n` +
                `Tamanho total: ${(totalSize / 1024).toFixed(1)} KB\n` +
                `Tags únicas: ${tagCounts.size}\n\n` +
                `Top 10 tags:\n${topTags || "Nenhuma tag"}`
        }],
      };
    }

    default:
      throw new Error("Ferramenta desconhecida");
  }
});

// Resources implementation
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [
      {
        uri: "vault://Bem-vindo.md",
        name: "Bem-vindo ao Vault",
        description: "Página inicial do hub de projetos",
        mimeType: "text/markdown",
      },
    ],
  };
});

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  if (request.params.uri === "vault://Bem-vindo.md") {
    const content = fs.readFileSync(path.join(VAULT_ROOT, "Bem-vindo.md"), "utf-8");
    return {
      contents: [{ uri: request.params.uri, mimeType: "text/markdown", text: content }],
    };
  }
  throw new Error("Recurso não encontrado");
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Will Obsidian MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Erro fatal:", error);
  process.exit(1);
});