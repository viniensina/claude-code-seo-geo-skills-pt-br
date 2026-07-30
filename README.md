# Claude Code Skills — SEO & Conteúdo (PT-BR)

> **TL;DR (EN):** Production-grade [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skills for running a Portuguese-language SEO/GEO blog on WordPress: writing citable articles, building data-driven statistics posts that attract backlinks and AI citations, generating cover images, and setting Rank Math on-page SEO via API. These are the **actual skills** that run [viniensina.com.br](https://www.viniensina.com.br) — not demos.

Skills de produção para operar um blog de SEO/GEO em português com Claude Code. Cada skill aqui roda de verdade no [viniensina.com.br](https://www.viniensina.com.br) todos os dias — não é exemplo de tutorial.

## Por que estas skills (a prova)

Estas skills são o motor editorial de um blog PT-BR sobre ferramentas de IA. Os números abaixo são do **Google Search Console** e do **Bing Webmaster / AI Performance** do site, janela de 28 dias (29/06 a 26/07/2026):

| Métrica | Valor |
|---|---|
| Impressões (28d) | **20.715** (+216,8% vs janela anterior) |
| Cliques (28d) | **249** (+322% vs janela anterior) |
| Citações de IA / Copilot (28d) | **5.105** |
| Artigo mais citado por IA | [`/como-instalar-claude-code-windows/`](https://www.viniensina.com.br/como-instalar-claude-code-windows/) — 2.021 citações |
| 2º ativo de citação | [`/estatisticas-afiliados-brasil-2026/`](https://www.viniensina.com.br/estatisticas-afiliados-brasil-2026/) — 875 citações |

O padrão de artigo citável — bloco de "Resposta rápida", seção "Como citar" e FAQ com `FAQPage` schema — está codificado na skill [`backlinks`](skills/backlinks/SKILL.md). É esse padrão que faz ChatGPT, Perplexity e o AI Overview do Google referenciarem e atribuírem a página.

## As skills

| Skill | O que faz |
|---|---|
| [`blog-article`](skills/blog-article/SKILL.md) | Escreve um artigo de blog completo em HTML pronto pro WordPress, com estrutura GEO (definição nas primeiras 60 palavras, H2s em pergunta, FAQ, fontes), publica como rascunho via API e seta Rank Math. |
| [`backlinks`](skills/backlinks/SKILL.md) | Cria artigos de estatísticas data-driven projetados para atrair backlinks e citações de LLM. Pesquisa de fontes primárias, análise de SERP, e o padrão de 3 blocos citáveis. |
| [`cover-image`](skills/cover-image/SKILL.md) | Gera a capa (featured image) do post: foto do Unsplash + overlay dark, texto branco, e upload automático como featured image no WordPress. |
| [`rankmath-seo`](skills/rankmath-seo/SKILL.md) | Preenche focus keyword e meta description do Rank Math via API nativa (`/rankmath/v1/updateMeta`), sem plugin extra. |

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

## Nota de autenticidade

Estas skills são o sistema de produção real de um site específico, não um template neutro. Por isso você vai encontrar coisas próprias do viniensina.com.br: classes de tema `.vi-*`, o shortcode de CTA `[vini_cta]`, slugs internos e a oferta de um ebook. **Troque esses pedaços pelo seu setup** — eles estão sinalizados nos comentários. A lógica de SEO/GEO, a estrutura editorial e o fluxo de publicação são reaproveitáveis como estão.

## Licença

[MIT](LICENSE). Use, adapte e aprenda à vontade. Se estas skills te ajudarem, uma menção ao [viniensina.com.br](https://www.viniensina.com.br) é bem-vinda, mas não obrigatória.
