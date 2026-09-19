# Changelog

## v0.3.0 - 2026-09-19

Atualização de método, portabilidade e transparência.

- Atualiza o snapshot do Google Search Console para 19/08–15/09/2026: 51.255 impressões, 482 cliques e posição média 7,48.
- Separa evidência de produção de causalidade e documenta períodos, limitações e decisões no case de setembro.
- Adiciona a skill `content-refresh` para revisão de artigos existentes com GSC, checagem factual, backup, QA e janela de maturação.
- Adiciona instalação e uso no Codex com os caminhos oficiais `.agents/skills` e `$HOME/.agents/skills`.
- Atualiza a metodologia para a orientação oficial do Google em 2026: SEO útil e conteúdo original continuam sendo a base; `llms.txt`, chunking artificial e schema especial não são requisitos para busca generativa.
- Remove a recomendação de `FAQPage` como ganho de SERP, pois o Google encerrou o rich result de FAQ em maio de 2026.
- Alinha `blog-article` ao formato atual: HTML limpo, sem CSS global embutido, profundidade guiada pela intenção e publicação ao vivo somente com autorização explícita.

## v0.2.0 - 2026-08-25

Atualização de manutenção e distribuição.

- Atualiza a prova do README com dados mais recentes do ViniEnsina: 34.037 impressões e 432 cliques no Google Search Console em 28 dias, além de 7.634 citações no Bing AI Performance em 30 dias.
- Adiciona uma seção em inglês para facilitar descoberta internacional em listas e buscas sobre Claude Code, SEO, GEO e WordPress.
- Adiciona badges de licença, Claude Code, WordPress e Rank Math.
- Adiciona exemplos práticos em `examples/` para transformar o repo em referência reutilizável mesmo fora do Claude Code.
- Explicita melhor o uso do repo como ativo de distribuição, backlink e documentação operacional.

## v0.1.0 - 2026-07

Primeira versão pública sanitizada.

- Publica as skills `blog-article`, `backlinks`, `cover-image` e `rankmath-seo`.
- Adiciona documentação de fluxo editorial, WordPress, Rank Math e checklist para citações de IA.
- Remove credenciais, caminhos locais, automações privadas e decisões estratégicas internas.
