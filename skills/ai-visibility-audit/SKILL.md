---
name: ai-visibility-audit
description: Analisa exportações do Bing AI Performance para medir citações, páginas, grounding queries e sobreposição entre snapshots. Use em auditorias de visibilidade em IA, acompanhamento GEO ou comparação de janelas móveis. Não use para escrever o artigo nem para prometer causalidade, ranking ou tráfego.
---

# AI Visibility Audit

Transforme exportações do Bing AI Performance em uma auditoria reproduzível, distinguindo tendência observada de causalidade.

## Inputs

Peça os CSVs disponíveis, sem exigir todos para começar:

- **Overview:** datas, citações e páginas citadas;
- **Pages:** URLs e citações;
- **Grounding queries:** consulta agrupada, intent, topic, citações e Citation Share;
- um segundo conjunto equivalente, quando o usuário quiser comparar snapshots.

Preserve os arquivos originais. Não publique CSVs privados sem autorização; use apenas agregados ou exemplos sanitizados.

## Fluxo

1. Confirme o filtro selecionado e derive o período das datas realmente retornadas pelo Overview.
2. Execute `scripts/analyze_ai_visibility.py` para produzir Markdown e JSON. Use `--previous-*` somente com arquivos da mesma propriedade e dimensão.
3. Leia o relatório e, se houver comparação, destaque a sobreposição antes de comentar deltas.
4. Classifique recomendações editoriais como hipóteses:
   - **defender:** páginas líderes que precisam permanecer corretas e atualizadas;
   - **expandir:** temas ou formatos com crescimento e consultas relacionadas;
   - **recuperar:** URLs presentes nos dois snapshots com queda observada;
   - **testar:** oportunidade editorial ainda sem evidência suficiente.
5. Se houver GSC ou analytics, analise essas fontes separadamente e só depois faça o cruzamento por URL. Não some métricas entre plataformas.
6. Entregue prioridades, limitações e a próxima data de medição. Não altere conteúdo ou publique no site sem autorização específica.

Exemplo:

```bash
python skills/ai-visibility-audit/scripts/analyze_ai_visibility.py \
  --overview exports/overview.csv \
  --pages exports/pages.csv \
  --queries exports/queries.csv \
  --previous-overview exports/overview-anterior.csv \
  --previous-pages exports/pages-anterior.csv \
  --output auditoria.md \
  --json-output auditoria.json
```

No PowerShell, use a linha única ou substitua `\` por crase.

## Guardrails

- Compare totais sobrepostos como **snapshots móveis**, não como períodos independentes.
- Não chame a diferença de duas janelas móveis de “citações líquidas adquiridas”.
- Linha ausente em Pages ou Grounding queries significa **não retornada**, não zero.
- Overview, Pages e Grounding queries podem ter totais diferentes por agregação e amostragem.
- Citação não equivale a clique, sessão, conversão, ranking, backlink ou autoridade.
- Citation Share vale para o contexto da consulta e da amostra da plataforma; não é market share geral.
- Intent e Topic são classificações da plataforma, sujeitas a ausência ou erro.
- Para atribuir uma mudança, registre edição, recrawl e uma janela posterior comparável; mesmo assim, use linguagem observacional sem desenho causal.

Leia [`references/interpretation.md`](references/interpretation.md) quando houver snapshots sobrepostos, linhas ausentes ou necessidade de combinar o Bing com outras fontes.

