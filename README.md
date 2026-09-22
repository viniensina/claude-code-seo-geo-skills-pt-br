# Agent Skills — SEO, GEO & WordPress (PT-BR)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-blue)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Agent%20Skills-111827)](https://developers.openai.com/pt-BR/docs/build-skills)
[![WordPress](https://img.shields.io/badge/WordPress-REST%20API-21759b)](https://developer.wordpress.org/rest-api/)
[![Rank Math](https://img.shields.io/badge/Rank%20Math-SEO-orange)](docs/rank-math-api.md)

> **TL;DR (EN):** Production-grade Agent Skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [Codex](https://developers.openai.com/pt-BR/docs/build-skills), built around a real Portuguese-language WordPress SEO workflow. They cover new articles, evidence-led content refreshes, data-backed citation assets, cover images, and Rank Math metadata. These are sanitized versions of workflows used on [viniensina.com.br](https://www.viniensina.com.br), not ranking guarantees.

Skills de produção para operar um blog de SEO/GEO em português com Claude Code ou Codex. O repositório publica versões sanitizadas de fluxos usados no [viniensina.com.br](https://www.viniensina.com.br), com limites explícitos entre evidência, hipótese e resultado.

> Atualizado em setembro de 2026. Veja o histórico em [`CHANGELOG.md`](CHANGELOG.md).

## Evidência de produção

Estas skills são parte do motor editorial de um blog PT-BR sobre ferramentas de IA, SEO e automação. Os números abaixo são do **Google Search Console**, do **Bing Webmaster / AI Performance** e do **GA4** do site:

| Métrica | Valor |
|---|---|
| Google Search Console, 28d (23/08 a 19/09/2026) | **53.371 impressões** e **488 cliques** |
| Crescimento vs janela anterior equivalente | **+58,5%** em impressões e **+13,0%** em cliques |
| Média diária no Google | **1.906,1 impressões/dia** |
| Posição média | **7,44**, ante **8,39** na janela anterior (menor é melhor) |
| Bing AI Performance, exportação de 30d com 29 datas (23/08 a 20/09/2026) | **16.648 citações** em Microsoft Copilots and Partners |
| Ritmo recente no Bing AI | **3.563 citações** nos últimos 7 dias, **+19,2%** vs 7 dias anteriores |
| Página líder no Bing AI | [`/claude-sonnet-opus-haiku-diferenca/`](https://www.viniensina.com.br/claude-sonnet-opus-haiku-diferenca/) — **4.305 citações** |
| Venda atribuída a IA | Compra real de R$19,90 após recomendação do ChatGPT, validada por GA4 + KV em 25/08/2026 |

Esses números descrevem o site inteiro e **não provam causalidade** de uma skill isolada. Citação também não equivale a clique, sessão, ranking ou autoridade. Os dados demonstram uso em produção e oferecem uma linha de base auditável. Veja períodos e limitações em [`docs/case-study-september-2026.md`](docs/case-study-september-2026.md) e o protocolo de exportação em [`docs/bing-ai-performance-methodology.md`](docs/bing-ai-performance-methodology.md).

O padrão de conteúdo citável — resposta direta, dados rastreáveis, metodologia, fontes primárias e atribuição clara — está codificado na skill [`backlinks`](skills/backlinks/SKILL.md). Ele não promete ranking, backlink ou citação automática; reduz o atrito para leitores e sistemas que precisam verificar e atribuir uma informação.

## For English readers

This repository is intentionally written in Portuguese because the workflow was built for a Brazilian WordPress site. You can still reuse the structure if you publish in another language:

- use `skills/backlinks/SKILL.md` as a blueprint for citable, data-driven articles;
- use `skills/content-refresh/SKILL.md` to audit and refresh existing pages without resetting the measurement window;
- use `docs/ai-citation-checklist.md` as an AI visibility and citation checklist;
- use `docs/wordpress-publishing-flow.md` as a safe WordPress draft workflow;
- replace ViniEnsina-specific CSS classes, CTA shortcodes, internal links and branding with your own setup.

The project is a real production workflow, not a neutral template. Treat it as an opinionated reference implementation.

## As skills

| Skill | O que faz |
|---|---|
| [`blog-article`](skills/blog-article/SKILL.md) | Cria posts novos com pesquisa, conteúdo não comoditizado, HTML limpo, metadados e rascunho seguro no WordPress. |
| [`backlinks`](skills/backlinks/SKILL.md) | Cria artigos de estatísticas verificáveis com fontes primárias, metodologia e atribuição clara, sem prometer backlinks ou citações. |
| [`content-refresh`](skills/content-refresh/SKILL.md) | Audita e atualiza artigos existentes com evidência de GSC, checagem factual, decisão entre ajuste cirúrgico e reconstrução, QA e janela de maturação. |
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
| [`Case de setembro de 2026`](docs/case-study-september-2026.md) | Snapshot auditável do GSC e exemplos de como os sinais foram usados para priorizar revisões — sem confundir execução com resultado. |
| [`Metodologia do Bing AI Performance`](docs/bing-ai-performance-methodology.md) | Como exportar, comparar e interpretar citações, páginas, consultas, intents e Citation Share sem extrapolar o dado. |

## Requisitos

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) ou [Codex](https://developers.openai.com/pt-BR/docs/build-skills).
- Um site **WordPress** com a REST API ativa e um [Application Password](https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/).
- **Rank Math SEO** (para a skill `rankmath-seo`).
- **Python 3.9+** com `requests` e `Pillow` (para a skill `cover-image` e os scripts):
  ```bash
  pip install requests Pillow
  ```
  Opcional: `python-dotenv` (`pip install python-dotenv`) para carregar o `.env` automaticamente. Sem ele, os scripts usam as variáveis que você exportar no ambiente (ver [Configuração](#configuração)).
- Uma chave de API do [Unsplash](https://unsplash.com/developers) (para a skill `cover-image`).

## Instalação no Claude Code

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

## Instalação no Codex

O Codex lê skills de projeto em `.agents/skills` e skills pessoais em `$HOME/.agents/skills`, conforme a [documentação oficial da OpenAI](https://developers.openai.com/pt-BR/docs/build-skills).

```bash
# Disponíveis apenas neste repositório:
mkdir -p .agents/skills
cp -r skills/* .agents/skills/

# OU disponíveis para o usuário em qualquer projeto:
mkdir -p "$HOME/.agents/skills"
cp -r skills/* "$HOME/.agents/skills/"
```

No Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse skills\* .agents\skills\

# OU no escopo do usuário:
New-Item -ItemType Directory -Force $HOME\.agents\skills | Out-Null
Copy-Item -Recurse skills\* $HOME\.agents\skills\
```

No Codex CLI ou na extensão para IDE, use `/skills` ou digite `$` para mencionar uma skill. Reinicie o Codex se uma skill recém-copiada não aparecer.

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

As skills podem ser acionadas implicitamente pela descrição ou mencionadas pelo nome. No Codex, use `$nome-da-skill`; no Claude Code, descreva a tarefa ou use o mecanismo de skills disponível na sua instalação.

| Skill | Peça algo como |
|---|---|
| `blog-article` | "Cria um artigo de blog sobre *como usar o n8n para marketing*, keyword `n8n para marketing`, foco em iniciante." |
| `backlinks` | "Faz um artigo de estatísticas sobre *IA em anúncios pagos 2026* pra atrair backlinks e citação de IA." |
| `content-refresh` | "Audita este artigo com os dados do GSC e aplica só as mudanças justificadas, preservando URL e conversão." |
| `cover-image` | "Gera a capa do post ID 1923 com uma foto de dashboard de anúncios." |
| `rankmath-seo` | "Preenche o focus keyword e a meta description do Rank Math do post 1923." |

Cada skill coleta apenas os inputs que realmente faltarem. As que criam posts usam **rascunho** (`status: draft`) por padrão; publicação ou alteração ao vivo exige autorização explícita do usuário.

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

## O que este projeto não promete

- Não existe estrutura de artigo que garanta ranking, backlink ou citação por IA.
- Para o Google, boas práticas tradicionais de SEO continuam sendo a base das experiências generativas; não há schema especial nem necessidade de `llms.txt` para aparecer nelas. Veja o [guia oficial do Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- O Google deixou de exibir rich results de FAQ em maio de 2026. FAQ ainda pode ajudar leitores, mas `FAQPage` não deve ser tratado como ganho de SERP. Veja o [histórico oficial](https://developers.google.com/search/updates#june-2026).
- Métricas do ViniEnsina são estudos de caso, não previsão de desempenho para outros sites.

## Nota de autenticidade

Estas skills são o sistema de produção real de um site específico, não um template neutro. Por isso você vai encontrar coisas próprias do viniensina.com.br: classes de tema `.vi-*`, o shortcode de CTA `[vini_cta]`, slugs internos e a oferta de um ebook. **Troque esses pedaços pelo seu setup** — eles estão sinalizados nos comentários. A lógica de SEO/GEO, a estrutura editorial e o fluxo de publicação são reaproveitáveis como estão.

## Licença

[MIT](LICENSE). Use, adapte e aprenda à vontade. Se estas skills te ajudarem, uma menção ao [viniensina.com.br](https://www.viniensina.com.br) é bem-vinda, mas não obrigatória.
