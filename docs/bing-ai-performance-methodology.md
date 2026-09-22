# Metodologia — Bing AI Performance

Protocolo para exportar e interpretar dados de visibilidade em IA no Bing Webmaster Tools sem confundir citações com tráfego ou causalidade.

## O que a métrica representa

O AI Performance report contabiliza citações visíveis do site em experiências de IA cobertas pelo Bing, como Microsoft Copilot, respostas de IA no Bing e parceiros selecionados. Segundo a documentação do Bing, os dados são amostrados e agregados.

Uma citação não é um clique. Ela também não comprova sessão, conversão, ranking, autoridade, backlink nem preferência geral de um modelo.

Referências oficiais:

- [Bing Webmaster Tools — AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)
- [Introducing AI Performance in Bing Webmaster Tools](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)

## Exportação reproduzível

1. Selecione o período na interface.
2. No mesmo momento, exporte **Overview**, **Pages** e **Grounding queries**.
3. Salve os arquivos sem editar, incluindo a data da coleta no nome ou no registro do experimento.
4. Verifique a primeira e a última data realmente retornadas pela visão geral. Um filtro de “30 dias” pode conter menos datas.
5. Registre filtros, fuso horário e qualquer mensagem de baixa atividade ou amostragem exibida pela plataforma.
6. Gere tabelas derivadas em arquivos separados; não altere os CSVs brutos.

Registro mínimo recomendado:

| Campo | Exemplo |
|---|---|
| Coleta | 22/09/2026 |
| Filtro selecionado | 30 dias |
| Datas realmente retornadas | 23/08–20/09/2026, 29 datas |
| Citações da visão geral | 16.648 |
| Linhas na visão de páginas | 85 |
| Linhas na visão de consultas | 191 |

## Como ler cada visão

### Overview

Use para tendência temporal, média diária e comparação entre recortes internos equivalentes. Picos devem ser investigados, não automaticamente atribuídos a uma publicação.

### Pages

Use para descobrir quais URLs aparecem como fonte. Concentração ajuda a priorizar manutenção e expansão de clusters, mas não demonstra que o formato da página causou a citação.

### Grounding queries

São frases agrupadas relacionadas ao processo de grounding. Não devem ser publicadas como se fossem o prompt completo e literal do usuário.

- **Citations:** ocorrências atribuídas à frase agrupada na exportação.
- **Citation Share:** participação do site dentro do contexto daquela consulta e da amostra da plataforma; não é market share geral.
- **Intent e Topic:** classificações úteis para segmentação, sujeitas a erro ou ausência.

## Regras de comparação

- Compare janelas com a mesma duração e, de preferência, sem sobreposição.
- Em exportações móveis sobrepostas, declare a sobreposição. O delta por página não é aquisição líquida de citações.
- Ausência de uma página ou consulta no novo CSV não significa automaticamente zero.
- Não force a soma de Pages ou Grounding queries a coincidir com Overview. As dimensões podem usar agregação e amostragem diferentes.
- Não some citações do Bing com métricas do GSC, GA4 ou outras plataformas.
- Para avaliar uma edição, registre baseline, data da mudança, recrawl e janelas posteriores comparáveis.

## Snapshot validado em 22/09/2026

No ViniEnsina, a exportação selecionada como 30 dias retornou 29 datas, de 23/08 a 20/09/2026:

- 16.648 citações na visão geral;
- 574,1 citações por data, em média;
- 3.563 nos últimos 7 dias contra 2.988 nos 7 anteriores (+19,2%);
- 15.199 citações somadas na visão por página, diferença de 1.449 para o Overview;
- 11.197 citações nas cinco páginas líderes, 67,3% do total do Overview.

Esse snapshot é evidência observacional do site inteiro. Ele serve para priorização e acompanhamento, não para prometer que uma estrutura, skill ou edição produzirá o mesmo resultado em outro projeto.
