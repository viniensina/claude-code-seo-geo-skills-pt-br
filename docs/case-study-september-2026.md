# Estudo de caso — setembro de 2026

Snapshot de produção usado para documentar o método deste repositório. Os dados são do site inteiro e não isolam o efeito de uma skill, edição ou canal.

## Google Search Console

Fonte: exportação pela API do Google Search Console gerada em 21/09/2026.

| Métrica | 23/08–19/09/2026 | 26/07–22/08/2026 | Variação |
|---|---:|---:|---:|
| Impressões | 53.371 | 33.663 | +58,5% |
| Cliques | 488 | 432 | +13,0% |
| CTR | 0,91% | 1,28% | -0,37 p.p. |
| Posição média | 7,44 | 8,39 | melhora de 0,95 |
| Impressões/dia | 1.906,1 | 1.202,3 | +58,5% |

Leitura correta: a visibilidade e os cliques cresceram, enquanto o CTR caiu. Isso cria uma fila de trabalho para titles, metas e respostas iniciais, mas não prova que o CTR menor tenha uma causa única.

## Como os sinais viraram decisões

Algumas páginas com muitas impressões foram selecionadas para revisão em 19/09, depois do fim da janela acima:

| Página | Impressões | Cliques | Posição média | Uso do dado |
|---|---:|---:|---:|---|
| `/prompts-chatgpt-vendas/` | 3.010 | 43 | 8,14 | Revisão de exemplo, contexto, FAQ e alegações frágeis |
| `/claude-projects-o-que-sao-como-usar/` | 1.789 | 9 | 7,94 | Auditoria factual e reforço de links internos |
| `/custo-token-ia-2026/` | 1.551 | 17 | 6,86 | Auditoria integral de fatos e preços |

Essas revisões são **ações posteriores ao snapshot**, não resultados atribuíveis a elas. O efeito só pode ser discutido após recrawl e janelas comparáveis.

## Bing AI Performance

Fonte: três CSVs exportados do Bing Webmaster Tools em 22/09/2026: visão geral, páginas e grounding queries. A interface estava selecionada em 30 dias, mas a visão geral trouxe 29 datas, de 23/08 a 20/09/2026.

| Métrica | Valor |
|---|---:|
| Citações na visão geral | 16.648 |
| Média por data retornada | 574,1 |
| Últimos 7 dias | 3.563 |
| 7 dias anteriores | 2.988 |
| Variação entre os dois recortes | +19,2% |
| Páginas retornadas no CSV | 85 |
| Soma da visão por página | 15.199 |

As páginas mais citadas na exportação foram:

| Página | Citações |
|---|---:|
| `/claude-sonnet-opus-haiku-diferenca/` | 4.305 |
| `/precos-ferramentas-marketing-2026/` | 2.435 |
| `/estatisticas-afiliados-brasil-2026/` | 1.864 |
| `/como-instalar-claude-code-windows/` | 1.635 |
| `/como-instalar-codex-windows/` | 958 |

As cinco páginas somaram 11.197 citações, ou 67,3% do total da visão geral. Isso mostra concentração, não causalidade. Comparativos, preços, estatísticas e tutoriais aparecem entre os líderes, mas o snapshot sozinho não demonstra que o formato causou a seleção.

Entre as grounding queries agrupadas, `estatísticas recentes marketing de afiliados 2026` registrou 413 citações e Citation Share de 50,55%. O Bing informa que essas consultas representam frases agrupadas usadas no grounding, não necessariamente o prompt completo escrito pelo usuário.

O total por página ficou 1.449 abaixo da visão geral, e a soma das consultas também não coincide com o total. As visões são amostradas e agregadas de formas diferentes; não se deve preencher a diferença, tratar linha ausente como zero nem somar dimensões como se fossem uma tabela única. O protocolo completo está em [`bing-ai-performance-methodology.md`](bing-ai-performance-methodology.md).

## Limitações

- GSC agrega múltiplas mudanças, páginas, sazonalidade e atualizações dos sistemas de busca.
- Posição média e CTR são agregados; precisam de leitura por página e consulta.
- Citações de IA de uma plataforma não representam toda a busca generativa.
- Uma citação visível no Bing não equivale a clique, sessão, conversão, ranking ou backlink.
- Grounding queries são agrupamentos; podem não reproduzir o prompt original.
- Intents, Topics e Citation Share dependem da classificação e amostragem da plataforma.
- IndexNow aceito não comprova crawl, indexação ou ganho de posição.
- Correlação temporal não demonstra causalidade.

## Método de acompanhamento

1. Registrar baseline e horário da edição.
2. Preservar URL e elementos de conversão sem evidência para removê-los.
3. Confirmar recrawl posterior.
4. Evitar novas mudanças durante a maturação, salvo erro crítico.
5. Comparar janelas equivalentes de 7, 14 e 28 dias.
6. Documentar resultados positivos, negativos e inconclusivos.
