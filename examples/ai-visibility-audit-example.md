# Auditoria de visibilidade em IA

Propriedade: **example.com (dados sintéticos)**

## Escopo

- Período real retornado: **2026-09-01 a 2026-09-14** (14 datas).
- Citações no Overview: **1.990**.
- Média por data retornada: **142,1**.
- Últimas 7 datas: **1.210**; variação vs 7 anteriores: **+55,1%**.

## Comparação de snapshots

- Tipo: **janelas móveis sobrepostas**.
- Sobreposição: **5 dias** (35,7% da janela atual).
- Variação do total móvel: **832 (+71,8%)**.
- Esse delta não representa citações líquidas adquiridas quando há sobreposição.

## Páginas

O CSV retornou 5 páginas e soma 1.775 citações. Diferença para o Overview: 215. As cinco líderes representam 89,2% do Overview.

| Página | Citações |
|---|---:|
| `/comparativo-modelos/` | 620 |
| `/estatisticas-mercado/` | 480 |
| `/guia-instalacao/` | 310 |
| `/precos-ferramentas/` | 220 |
| `/automacao-marketing/` | 145 |

## Mudanças por página

Maiores altas entre URLs retornadas nos dois snapshots:

- `/comparativo-modelos/`: 80.
- `/estatisticas-mercado/`: 70.
- `/precos-ferramentas/`: 40.

Maiores quedas entre URLs retornadas nos dois snapshots:

- `/guia-instalacao/`: -20.

Não retornadas no atual: 1. Não retornadas no anterior: 1. Esses estados não foram convertidos em zero.

## Grounding queries

O CSV retornou 3 consultas legíveis e soma 655 citações. Diferença para o Overview: 1.335.

| Consulta agrupada | Intent | Topic | Citações | Citation Share |
|---|---|---|---:|---:|
| comparativo de modelos de ia | Comparison | Technology | 280 | 32,50% |
| estatísticas de mercado de ia 2026 | Research | Business | 230 | 41,20% |
| como instalar ferramenta de ia | Informational | Development Tools | 145 | 12,10% |

## Limitações

- Citação não equivale a clique, sessão, conversão, ranking, backlink ou autoridade.
- Totais de Overview, Pages e Grounding queries podem diferir por agregação e amostragem.
- Linha ausente em um snapshot significa não retornada, não zero.
- Grounding queries são frases agrupadas e podem não reproduzir o prompt completo.
- Mudanças temporais são observacionais e não demonstram causalidade de uma edição.
