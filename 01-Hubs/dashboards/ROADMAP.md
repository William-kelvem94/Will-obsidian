# ROADMAP CONHECIMENTO, INFRAESTRUTURA E AUTOMAÇÃO

## ÉPOCAS-CHAVE
- **v1.0** ✅ Padronização de base, dedupe, preprocess full (10.787 chunks), frontmatter mínimo, templates, scripts de enriquecimento
- **v1.1** ✅ Indexação incremental, auditoria de sensíveis, CI de recall de embeddings, gap scanning automático, interface web
- **v1.5** ✅ **Expansão massiva de conhecimento** — 21 novas notas, 11.201 linhas de conteúdo adicionadas em Humanidades, Exatas, Biológicas e Tech gaps
- **v2.0** 🔄 Integração com Zotero/citações, multimodalidade avançada, taxonomia viva (próximo)
- **v3.0** 🧠 Expansão colaborativa, contribuições externas, publicação seletiva

## STATUS DAS INICIATIVAS

### ✅ Concluído
- Padronização de frontmatter mínima (templates/scripts gerados)
- Enriquecimento de metadados (enrich_frontmatter.py)
- Preprocess completo do vault (10.787 chunks em preprocess_full.jsonl)
- Branch feature/preprocess-and-infra com commit detalhado e push
- Scripts: dedupe, preprocess, frontmatter, sensitive, patches, snippets
- Geração de ROADMAP.md, TAXONOMY.md, GAPS.md, BIBLIOGRAFIA.md, MULTIMODALIDADE.md, SEGURANCA_PRIVACIDADE.md, ANALYTICS.md
- Scripts de expansão: preprocess_incremental.py, gen_skill.py, gen_analytics.py, preprocess_multimodal.py, scan_gaps.py
- Workflow CI: test_embedding_retrieval.yml
- Integração de audit_sensitives.py e enrich_frontmatter.py no pre-commit-config.yaml
- Demonstração via gen_skill.py: "Explainable AI" criada com frontmatter padronizado

### ✅ Concluído (Expansão Sprint)
- **História**: Mundial (547 linhas) + Brasil (408 linhas) — `Conhecimento-Geral/Historia/`
- **Ciência Política**: 659 linhas — `Conhecimento-Geral/Ciencia-Politica.md`
- **Sociologia expandida**: Teorias-Sociologicas (772 linhas) — `Conhecimento-Geral/Cultura/`
- **Arte e Estética**: 649 linhas — `Conhecimento-Geral/Cultura/Estetica-e-Arte.md`
- **Antropologia Cultural**: 459 linhas — `Conhecimento-Geral/Cultura/`
- **Física**: Fundamental (633) + Quântica (417) — `Conhecimento-Geral/Fisica/`
- **Química Geral**: 493 linhas — `Conhecimento-Geral/Quimica/`
- **Biologia**: Celular/Molecular (697) + Evolução/Genética (514) + Fisiologia (540) — `Conhecimento-Geral/Biologia/`
- **Psicologia Clínica**: 526 linhas — `Conhecimento-Geral/Psicologia/`
- **Matemática expandida**: Discreta (527) + Equações Diferenciais (640) — `Conhecimento-Geral/Matematica/`
- **Filosofia expandida**: Política (598) + Epistemologia (553) — `Conhecimento-Geral/Filosofia/`
- **Mobile Development**: 1075 linhas — `skills/mobile/`
- **Computer Vision**: 739 linhas — `skills/ai/`
- **LLM Fine-Tuning**: 616 linhas — `skills/ai/`
- **LLMOps**: 925 linhas — `skills/ai/`
- **Automações Cognitivas**:
  - `scripts/zotero_integrator.py`: Sincronização e fichamento automatizado de artigos acadêmicos diretamente do Zotero em `Conhecimento-Geral/Literatura/`.
  - `scripts/gen_bibliography.py`: Compilador de referências bibliográficas por DOI, BibTeX e frontmatter re-escrevendo dashboards/BIBLIOGRAFIA.md.
  - `scripts/generate_flashcards.py`: Processamento semântico de Conhecimento-Geral extraindo 3.203 cartões para Anki/CSV.

### 📋 Pendente
- Aplicar patches de frontmatter automaticamente (após validação)
- Revisão de qualidade das novas notas (algumas podem precisar de ajustes finos)
- Taxonomia viva e dinâmica
- Publicação seletiva de partes do vault

## MÉTRICAS DO VAULT
- 854+ arquivos .md (21 notas novas adicionadas)
- 386 patches de frontmatter gerados
- 95 grupos de duplicados detectados
- 10.787 chunks RAG gerados
- 11.201 linhas de novo conteúdo (expansão de conhecimento)
- 38 gaps de conhecimento identificados (após expansão)
- Tags: mais de 700 tags únicas mapeadas
- Top tags: projetos (98), jarvis (92), skills (51), conhecimento (47), hub (28)

---
*Este roadmap é atualizado manualmente e reflete as prioridades atuais do Will-obsidian.*
