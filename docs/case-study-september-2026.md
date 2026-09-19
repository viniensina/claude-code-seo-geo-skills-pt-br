# Estudo de caso — setembro de 2026

Snapshot de produção usado para documentar o método deste repositório. Os dados são do site inteiro e não isolam o efeito de uma skill, edição ou canal.

## Google Search Console

Fonte: exportação pela API do Google Search Console em 18/09/2026.

| Métrica | 19/08–15/09/2026 | 22/07–18/08/2026 | Variação |
|---|---:|---:|---:|
| Impressões | 51.255 | 32.135 | +59,5% |
| Cliques | 482 | 425 | +13,4% |
| CTR | 0,94% | 1,32% | -0,38 p.p. |
| Posição média | 7,48 | 8,66 | melhora de 1,18 |
| Impressões/dia | 1.830,5 | 1.147,7 | +59,5% |

Leitura correta: a visibilidade e os cliques cresceram, enquanto o CTR caiu. Isso cria uma fila de trabalho para titles, metas e respostas iniciais, mas não prova que o CTR menor tenha uma causa única.

## Como os sinais viraram decisões

Algumas páginas com muitas impressões foram selecionadas para revisão em 19/09, depois do fim da janela acima:

| Página | Impressões | Cliques | Posição média | Uso do dado |
|---|---:|---:|---:|---|
| `/prompts-chatgpt-vendas/` | 2.776 | 43 | 8,18 | Revisão de exemplo, contexto, FAQ e alegações frágeis |
| `/claude-projects-o-que-sao-como-usar/` | 1.764 | 9 | 8,00 | Auditoria factual e reforço de links internos |
| `/custo-token-ia-2026/` | 1.552 | 24 | 6,82 | Auditoria integral de fatos e preços |

Essas revisões são **ações posteriores ao snapshot**, não resultados atribuíveis a elas. O efeito só pode ser discutido após recrawl e janelas comparáveis.

## Bing AI Performance

O último snapshot disponível no momento desta release foi lido em 09/08/2026 e cobria 30 dias:

- 7.634 citações em Microsoft Copilots and Partners;
- 2.164 citações nos últimos 7 dias da janela;
- 1.300 nos primeiros 7 dias;
- variação de +66,5% entre esses recortes.

O dado é mantido com sua data original. Não foi extrapolado para setembro.

## Limitações

- GSC agrega múltiplas mudanças, páginas, sazonalidade e atualizações dos sistemas de busca.
- Posição média e CTR são agregados; precisam de leitura por página e consulta.
- Citações de IA de uma plataforma não representam toda a busca generativa.
- IndexNow aceito não comprova crawl, indexação ou ganho de posição.
- Correlação temporal não demonstra causalidade.

## Método de acompanhamento

1. Registrar baseline e horário da edição.
2. Preservar URL e elementos de conversão sem evidência para removê-los.
3. Confirmar recrawl posterior.
4. Evitar novas mudanças durante a maturação, salvo erro crítico.
5. Comparar janelas equivalentes de 7, 14 e 28 dias.
6. Documentar resultados positivos, negativos e inconclusivos.
