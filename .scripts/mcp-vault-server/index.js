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

const VAULT_ROOT = "D:/Documents/GitHub/Will-obsidian";

const server = new Server(
  {
    name: "will-obsidian-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      resources: {},
      tools: {},
    },
  }
);

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
    ],
  };
});

// Tool handlers
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "read_vault_file": {
      const filePath = path.join(VAULT_ROOT, args.relativePath);
      if (!filePath.startsWith(VAULT_ROOT)) throw new Error("Acesso negado");
      if (!fs.existsSync(filePath)) throw new Error("Arquivo não encontrado");
      
      const content = fs.readFileSync(filePath, "utf-8");
      return {
        content: [{ type: "text", text: content }],
      };
    }

    case "list_vault_files": {
      const targetDir = args.subFolder ? path.join(VAULT_ROOT, args.subFolder) : VAULT_ROOT;
      if (!targetDir.startsWith(VAULT_ROOT)) throw new Error("Acesso negado");
      
      const files = fs.readdirSync(targetDir, { recursive: true })
        .filter(f => !f.includes(".git") && !f.includes(".obsidian"));
        
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
              if (fs.statSync(fullPath).isDirectory()) {
                  if (file !== ".git" && file !== ".obsidian") getAllFiles(fullPath);
              } else if (file.endsWith(".md")) {
                  const content = fs.readFileSync(fullPath, "utf-8");
                  if (content.toLowerCase().includes(query)) {
                      results.push(path.relative(VAULT_ROOT, fullPath));
                  }
              }
          });
      };
      getAllFiles(VAULT_ROOT);
      return {
        content: [{ type: "text", text: `Resultados encontrados em:\n${results.join("\n")}` }],
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
