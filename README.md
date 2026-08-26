# Claude Code Skills — SEO & Conteúdo (PT-BR)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-blue)](https://docs.anthropic.com/en/docs/claude-code)
[![WordPress](https://img.shields.io/badge/WordPress-REST%20API-21759b)](https://developer.wordpress.org/rest-api/)
[![Rank Math](https://img.shields.io/badge/Rank%20Math-SEO-orange)](docs/rank-math-api.md)

> **TL;DR (EN):** Production-grade [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skills for running a Portuguese-language SEO/GEO blog on WordPress: writing citable articles, building data-driven statistics posts that attract backlinks and AI citations, generating cover images, and setting Rank Math on-page SEO via API. These are the **actual skills** that run [viniensina.com.br](https://www.viniensina.com.br) — not demos.

Skills de produção para operar um blog de SEO/GEO em português com Claude Code. Cada skill aqui roda de verdade no [viniensina.com.br](https://www.viniensina.com.br) todos os dias — não é exemplo de tutorial.

> Atualizado em agosto de 2026. Veja o histórico em [`CHANGELOG.md`](CHANGELOG.md).

## Por que estas skills (a prova)

Estas skills são parte do motor editorial de um blog PT-BR sobre ferramentas de IA, SEO e automação. Os números abaixo são do **Google Search Console**, do **Bing Webmaster / AI Performance** e do **GA4** do site:

| Métrica | Valor |
|---|---|
| Google Search Console, 28d (27/07 a 23/08/2026) | **34.037 impressões** e **432 cliques** |
| Crescimento vs janela anterior | **+59,8%** em impressões e **+66,2%** em cliques |
| Média diária no Google | **1.215,6 impressões/dia** |
| Bing AI Performance, 30d (leitura 09/08/2026) | **7.634 citações** em Microsoft Copilots and Partners |
| Crescimento em IA | **+66,5%** comparando primeiros 7 dias vs últimos 7 dias da janela |
| Página Claude mais citada por IA | [`/claude-sonnet-opus-haiku-diferenca/`](https://www.viniensina.com.br/claude-sonnet-opus-haiku-diferenca/) — 3.339 citações |
| Tutorial Claude Code mais citado por IA | [`/como-instalar-claude-code-windows/`](https://www.viniensina.com.br/como-instalar-claude-code-windows/) — 2.321 citações |
| Venda atribuída a IA | Compra real de R$19,90 após recomendação do ChatGPT, validada por GA4 + KV em 25/08/2026 |

O padrão de artigo citável — bloco de "Resposta rápida", seção "Como citar", dados rastreáveis e FAQ com `FAQPage` schema — está codificado na skill [`backlinks`](skills/backlinks/SKILL.md). Esse padrão não promete ranking, backlink ou citação automática, mas reduz o atrito para humanos e sistemas de IA entenderem, reutilizarem e atribuírem uma página.

## For English readers

This repository is intentionally written in Portuguese because the workflow was built for a Brazilian WordPress site. You can still reuse the structure if you publish in another language:

- use `skills/backlinks/SKILL.md` as a blueprint for citable, data-driven articles;
- use `docs/ai-citation-checklist.md` as an AI visibility and citation checklist;
- use `docs/wordpress-publishing-flow.md` as a safe WordPress draft workflow;
- replace ViniEnsina-specific CSS classes, CTA shortcodes, internal links and branding with your own setup.

The project is a real production workflow, not a neutral template. Treat it as an opinionated reference implementation.

## As skills

| Skill | O que faz |
|---|---|
| [`blog-article`](skills/blog-article/SKILL.md) | Escreve um artigo de blog completo em HTML pronto pro WordPress, com estrutura GEO (definição nas primeiras 60 palavras, H2s em pergunta, FAQ, fontes), publica como rascunho via API e seta Rank Math. |
| [`backlinks`](skills/backlinks/SKILL.md) | Cria artigos de estatísticas data-driven projetados para atrair backlinks e citações de LLM. Pesquisa de fontes primárias, análise de SERP, e o padrão de 3 blocos citáveis. |
| [`cover-image`](skills/cover-image/SKILL.md) | Gera a capa (featured image) do post: foto do Unsplash + overlay dark, texto branco, e upload automático como featured image no WordPress. |
| [`rankmath-seo`](skills/rankmath-seo/SKILL.md) | Preenche focus keyword e meta description do Rank Math via API nativa (`/rankmath/v1/updateMeta`), sem plugin extra. |

## Reutilize mesmo sem Claude Code

Mesmo que você não use Claude Code, dá para reaproveitar partes deste repo como checklist e documentação operacional:

| Recurso | Para que serve |
|---|---|
| [`AI citation checklist`](docs/ai-citation-checklist.md) | Checklist para transformar um artigo em ativo mais fácil de citar por IA, blogs e newsletters. |
| [`WordPress publishing flow`](docs/wordpress-publishing-flow.md) | Fluxo seguro para rascunho, mídia, Rank Math, QA e publicação no WordPress. |
| [`Rank Math API notes`](docs/rank-math-api.md) | Snippets e cuidados para atualizar SEO on-page via API nativa do Rank Math. |
| [`examples/`](examples/) | Exemplos de brief, artigo citável e checklist preenchido para adaptar no seu projeto. |

## Requisitos

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) instalado.
- Um site **WordPress** com a REST API ativa e um [Application Password](https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/).
- **Rank Math SEO** (para a skill `rankmath-seo`).
- **Python 3.9+** com `requests` e `Pillow` (para a skill `cover-image` e os scripts):
  ```bash
  pip install requests Pillow
  ```
  Opcional: `python-dotenv` (`pip install python-dotenv`) para carregar o `.env` automaticamente. Sem ele, os scripts usam as variáveis que você exportar no ambiente (ver [Configuração](#configuração)).
- Uma chave de API do [Unsplash](https://unsplash.com/developers) (para a skill `cover-image`).

## Instalação

Copie as skills que quiser para a sua pasta de skills do Claude Code:

```bash
# Globais (todos os projetos):
cp -r skills/* ~/.claude/skills/

# OU só para o projeto atual:
cp -r skills/* .claude/skills/
```

No Windows (PowerShell):

```powershell
Copy-Item -Recurse skills\* $HOME\.claude\skills\
```

## Configuração

Nenhuma credencial fica no código. Copie o exemplo e preencha com os seus valores:

```bash
cp .env.example .env
```

```dotenv
WP_URL=https://seusite.com
WP_USER=seu-usuario-wp
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx
UNSPLASH_KEY=sua-chave-unsplash
```

> `WP_USER` é o **nome de usuário (login)** do WordPress. Use o e-mail apenas se ele for o seu login de fato — Application Passwords autenticam pelo `user_login`, não pelo e-mail.

A skill `cover-image` aceita ainda variáveis **opcionais** de branding/fonte da capa — `COVER_BRAND`, `COVER_FONT_BOLD`, `COVER_FONT_REG`. Se omitidas, o script usa os defaults por SO. Veja os exemplos comentados no [`.env.example`](.env.example).

Os scripts carregam o `.env` automaticamente via `python-dotenv` (procuram na raiz do repo e no diretório onde você rodar o comando). Se preferir não usar `.env`, basta exportar as variáveis no ambiente:

```bash
# Linux/Mac
export WP_URL="https://seusite.com" WP_USER="seu-usuario" WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx" UNSPLASH_KEY="sua-chave"
```

```powershell
# Windows (PowerShell)
$env:WP_URL="https://seusite.com"; $env:WP_USER="seu-usuario"; $env:WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"; $env:UNSPLASH_KEY="sua-chave"
```

**Nunca** faça commit do seu `.env` (já está no `.gitignore`).

## Como usar

As skills são acionadas em linguagem natural dentro do Claude Code — descreva a tarefa e o Claude escolhe a skill pelo `description` de cada uma. Exemplos:

| Skill | Peça algo como |
|---|---|
| `blog-article` | "Cria um artigo de blog sobre *como usar o n8n para marketing*, keyword `n8n para marketing`, foco em iniciante." |
| `backlinks` | "Faz um artigo de estatísticas sobre *IA em anúncios pagos 2026* pra atrair backlinks e citação de IA." |
| `cover-image` | "Gera a capa do post ID 1923 com uma foto de dashboard de anúncios." |
| `rankmath-seo` | "Preenche o focus keyword e a meta description do Rank Math do post 1923." |

Cada skill pergunta os inputs que faltarem (tópico, keyword, categoria, ID do post) antes de rodar. As que publicam criam sempre um **rascunho** (`status: draft`) — você revisa antes de publicar.

## Exemplos práticos

A pasta [`examples/`](examples/) mostra como o método fica fora do abstrato:

- [`brief-exemplo.md`](examples/brief-exemplo.md): briefing de artigo antes da escrita;
- [`artigo-citavel-exemplo.md`](examples/artigo-citavel-exemplo.md): estrutura de página citável, com resposta rápida, tabela, metodologia, como citar e FAQ;
- [`checklist-ai-citations-preenchido.md`](examples/checklist-ai-citations-preenchido.md): checklist aplicado antes de publicar.

Use esses arquivos como ponto de partida para adaptar a lógica ao seu nicho, idioma e CMS.

## Distribuição e backlinks

Este repo também funciona como ativo de distribuição: ele documenta uma prática real, tem licença aberta e pode ser citado em listas, newsletters, artigos sobre Claude Code, SEO com IA, GEO, WordPress ou Rank Math.

Se você mantiver um fork ou adaptação, os pontos que mais ajudam outras pessoas a citar o projeto são:

- resultados próprios com janela e fonte declaradas;
- exemplos completos, não só prompts;
- changelog mostrando manutenção;
- instruções de instalação para Windows, macOS e Linux;
- documentação clara do que foi sanitizado e do que precisa ser adaptado.

## Nota de autenticidade

Estas skills são o sistema de produção real de um site específico, não um template neutro. Por isso você vai encontrar coisas próprias do viniensina.com.br: classes de tema `.vi-*`, o shortcode de CTA `[vini_cta]`, slugs internos e a oferta de um ebook. **Troque esses pedaços pelo seu setup** — eles estão sinalizados nos comentários. A lógica de SEO/GEO, a estrutura editorial e o fluxo de publicação são reaproveitáveis como estão.

## Licença

[MIT](LICENSE). Use, adapte e aprenda à vontade. Se estas skills te ajudarem, uma menção ao [viniensina.com.br](https://www.viniensina.com.br) é bem-vinda, mas não obrigatória.
