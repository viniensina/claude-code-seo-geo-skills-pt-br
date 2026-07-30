---
name: cover-image
description: Gera a capa (featured image) de posts do blog usando foto do Unsplash + overlay dark, e faz upload automático como featured image no WordPress. Use quando pedir para gerar capa de post, criar imagem de destaque, ou definir a featured image de um post WordPress. A parte mais importante é escolher a query certa pro Unsplash — pense como um editor de foto, não como uma busca genérica.
---

# cover-image — Gerador de Capa para Posts do Blog

> Skill de produção do viniensina.com.br. A paleta e o branding (`#7c3aed` roxo, domínio no rodapé) são do site — **troque pelos seus** via variáveis de ambiente e pelas constantes de cor no script.

**Output:** JPG 1200×675, overlay dark, texto branco, upload automático no WP como featured image.

Credenciais e chaves vêm do ambiente (ver `.env.example` na raiz do repo): `WP_URL`, `WP_USER`, `WP_APP_PASSWORD`, `UNSPLASH_KEY`. O script carrega o `.env` automaticamente via `python-dotenv`. Nunca hardcodar.

## Passo 1 — Coletar inputs

Se não foram fornecidos, perguntar:
- **Post ID** do WordPress (preferencial — busca o título automaticamente)
- OU **título** + **categoria** do artigo

## Passo 2 — Escolher a query do Unsplash (parte mais importante)

Pense como um **editor de fotografia**: qual foto ficaria bonita como capa desse artigo?

**Princípio:** a query deve descrever uma foto real e específica, não uma categoria abstrata.

| ❌ Genérico demais | ✅ Específico e visual |
|---|---|
| `artificial intelligence technology` | `advertising metrics screen dark` |
| `digital marketing` | `facebook ads manager laptop screen` |
| `social media` | `instagram analytics dashboard phone` |
| `ecommerce` | `online shopping cart checkout screen` |
| `seo` | `google search results laptop close up` |

**Raciocínio para escolher a query:**
1. Qual é o objeto/ação central do artigo? (ex: "anúncios pagos" → dashboard de ads)
2. Como esse objeto aparece visualmente? (tela, mão, laptop, gráfico, pessoa?)
3. Qual contexto de iluminação funciona com o overlay dark? (tela brilhante no escuro, ambiente de escritório, close em dispositivo)
4. A foto vai ter texto em cima — evitar fotos com texto próprio, rostos centrais ou fundo branco puro

**Exemplos por tema:**
- Meta Ads / anúncios pagos → `advertising analytics dashboard laptop screen`
- IA / ChatGPT → `chatgpt interface laptop screen dark`
- SEO → `google search console analytics screen`
- Email marketing → `email inbox laptop dark background`
- Copywriting → `person writing laptop coffee desk`
- Funil de vendas → `sales funnel conversion diagram screen`
- Afiliado / renda online → `passive income laptop beach remote work`
- Instagram → `instagram feed phone hand scrolling`
- Automação → `automation workflow diagram screen`
- Estatísticas / dados → `data visualization dashboard dark screen`

Se a primeira query parecer genérica após ver o resultado, tente 2-3 variações mais específicas antes de decidir.

## Passo 3 — Rodar o script

O script está em `scripts/gerar_capa.py` nesta skill. Rodar com o Python do seu ambiente.

> **Caminho:** o comando abaixo assume que você está na **raiz do repo clonado**. Se instalou as skills globalmente (`~/.claude/skills/`), use `~/.claude/skills/cover-image/scripts/gerar_capa.py` (no Windows: `$HOME\.claude\skills\cover-image\scripts\gerar_capa.py`).

```bash
python "skills/cover-image/scripts/gerar_capa.py" \
  --post-id <ID> \
  --query "<query escolhida>" \
  --pill "<categoria>" \
  [--subtitle "<subtítulo opcional>"] \
  [--photo-index <0-9>]
```

**Flags disponíveis:**
- `--post-id` — ID do post WP (busca título e seta a featured image automaticamente)
- `--title` — usar se não tiver post ID
- `--pill` — texto do badge (ex: "IA Marketing", "Meta Ads", "SEO")
- `--query` — query do Unsplash **(obrigatório)**
- `--subtitle` — linha abaixo do título
- `--photo-index` — qual foto da lista usar (0 = primeira, 1 = segunda, etc.)
- `--no-upload` — só salva localmente, sem subir no WP

## Passo 4 — Avaliar e ajustar

Após rodar, informar ao usuário:
- Qual foto foi usada (fotógrafo + descrição)
- Onde foi salva localmente
- Se foi definida como featured image no WP

Se a foto não ficou boa, sugerir alternativas:
- Tentar `--photo-index 1` ou `--photo-index 2` (próximas fotos da mesma query)
- Tentar uma query diferente e rodar novamente

## Personalização (troque pelo seu visual)

No topo de `scripts/gerar_capa.py`:
- **Cores** — constantes `PURPLE`, `PURPLE_LT`, `WHITE`, `MUTED` (RGB). Ajuste para a paleta do seu site.
- **Branding do rodapé** — variável de ambiente `COVER_BRAND` (padrão: `seusite.com`).
- **Subtítulo padrão** — passe `--subtitle` ou ajuste o fallback no `make_cover`.
- **Fontes** — o script escolhe um default por SO (Windows / macOS / Linux). Sobrescreva com `COVER_FONT_BOLD` / `COVER_FONT_REG` se quiser outra fonte. Se o arquivo não existir, há fallback com aviso para a fonte padrão do PIL.
