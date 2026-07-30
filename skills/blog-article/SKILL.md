---
name: blog-article
description: Cria artigos de blog completos para WordPress — escreve o HTML no formato do tema, aplica otimizações GEO, publica como rascunho via API, seta Rank Math (keyword + meta desc) e gera/sobe a capa automaticamente. Usar sempre que o usuário quiser criar um novo post para o blog.
---

# blog-article — Criação de Artigos para WordPress

> Skill de produção do viniensina.com.br. Os pedaços específicos do site (classes `.vi-*`, shortcode `[vini_cta]`, slugs internos, oferta do ebook) estão sinalizados — **troque pelo seu setup**.

## Credenciais e ambiente

Credenciais vêm do ambiente (ver `.env.example` na raiz do repo): `WP_URL`, `WP_USER`, `WP_APP_PASSWORD`. Nunca hardcodar.

```
Python: use o interpretador do seu ambiente/venv
```

## Passo 1 — Coletar inputs

Se não foram fornecidos, perguntar:
- **Tópico** — o que o artigo vai cobrir
- **Keyword-alvo** — frase de 2-4 palavras que o Google mostraria para buscas desse tema
- **Ângulo** — diferencial em relação a outros artigos (ex: foco em dados reais, prompts práticos, guia iniciante)
- **Categoria** — ID da categoria WP (ajuste os IDs ao seu site)

**Links internos disponíveis** (usar 3-5 no artigo onde contextualmente relevante) — troque por slugs reais do seu site:
- `/exemplo-pilar-do-cluster/`
- `/exemplo-artigo-irmao/`
- `/exemplo-estatisticas-do-tema/`

**CTA padrão:** troque pela sua oferta. No viniensina é o Ebook "IA no Piloto Automático" via shortcode.

---

## Passo 2 — Escrever o artigo

### Estrutura obrigatória

1. `vi-badge` com categoria
2. `vi-lede` — parágrafo de abertura com gancho forte + stat
3. Parágrafo de definição nas primeiras 60 palavras: **"O que é X? É..."**
4. `vi-toc` — índice com H2s em formato de pergunta
5. `vi-highlights` — box com 5-7 bullets do que o leitor vai aprender
6. 5-7 seções com H2 em pergunta, H3s, tabelas ou listas quando útil
7. `vi-cta-mid` — CTA da oferta no meio do artigo
8. FAQ com 3-4 perguntas antes da conclusão
9. Conclusão com fluxo de 4 passos (`vi-step-list`)
10. Data de publicação no final

### Regras de escrita

- Começar parágrafos com dado ou afirmação direta — nunca com "A maioria..." ou "Muitos..."
- Parágrafos curtos: 1-4 frases
- Usar `vi-prompt-box` quando o artigo tiver exemplos de prompts
- Usar `vi-insight` para dicas práticas e links internos contextuais
- Fonte externa com dado específico obrigatória na seção 1
- Mínimo 2000 palavras
- **Proibido:** "alavancar", "navegar pelas complexidades", "no cenário atual", "vale ressaltar", "em um mundo onde", "revolucionar", "game-changer"

### Formato de saída — REGRAS CRÍTICAS

O artigo inteiro vai dentro de **um único bloco** `<!-- wp:html -->`.

**Nunca usar** blocos Gutenberg separados (`wp:paragraph`, `wp:heading`, etc.) — quebra o layout.

O tema injeta automaticamente: H1, featured image, sidebar, CTA, posts relacionados. **Não incluir nada disso.**

**CSS — somente propriedades estruturais:**
- Permitido: `padding`, `border`, `margin`, `font-size`, `font-weight`, `border-radius`, `display`, `line-height`
- **Proibido:** `color`, `background-color` nos boxes decorativos — o tema controla as cores do texto
- **Proibido:** `body{}`, `*{}`, `:root{}`, `header{}`, `.wp-block-*`
- Boxes usam **apenas borda lateral** (`border-left`) sem background — evita conflito de contraste com o tema

### CSS padrão (exemplo do viniensina — troque as classes/cores pelo seu tema)

```html
<style>
.vi-badge { display:inline-block; background:#7c3aed; color:#fff; font-size:.75rem; font-weight:700; letter-spacing:.06em; text-transform:uppercase; padding:.25rem .75rem; border-radius:999px; margin-bottom:1rem; }
.vi-lede { font-size:1.15rem; line-height:1.75; border-left:4px solid #7c3aed; padding:.75rem 1rem; margin-bottom:2rem; }
.vi-toc { border:1px solid #e2e8f0; border-radius:10px; padding:1.25rem 1.5rem; margin:2rem 0; }
.vi-toc h3 { font-size:.9rem; font-weight:700; text-transform:uppercase; letter-spacing:.05em; margin:0 0 .75rem; }
.vi-toc ol { margin:0; padding-left:1.25rem; }
.vi-toc li { margin:.35rem 0; font-size:.95rem; }
.vi-toc a { text-decoration:none; }
.vi-highlights { border-left:4px solid #16a34a; padding:.75rem 1rem; margin:2rem 0; }
.vi-highlights h3 { font-size:1rem; font-weight:700; margin:0 0 .75rem; }
.vi-highlights ul { margin:0; padding-left:1.25rem; }
.vi-highlights li { margin:.4rem 0; font-size:.95rem; }
.vi-h2 { font-size:1.5rem; font-weight:700; margin:2.5rem 0 1rem; padding-bottom:.5rem; border-bottom:2px solid #e2e8f0; }
.vi-h3 { font-size:1.15rem; font-weight:700; margin:2rem 0 .75rem; }
.vi-insight { border-left:4px solid #fbbf24; padding:.85rem 1.1rem; margin:1.5rem 0; font-size:.97rem; }
.vi-prompt-box { background:#1e293b; border-radius:10px; padding:1.25rem 1.5rem; margin:1.5rem 0; }
.vi-prompt-box .vi-prompt-label { font-size:.7rem; font-weight:700; letter-spacing:.08em; text-transform:uppercase; color:#94a3b8; margin-bottom:.6rem; }
.vi-prompt-box pre { margin:0; white-space:pre-wrap; word-break:break-word; font-family:'Courier New',monospace; font-size:.88rem; line-height:1.65; color:#e2e8f0; }
.vi-step-list { list-style:none; padding:0; margin:1.5rem 0; counter-reset:steps; }
.vi-step-list li { counter-increment:steps; padding:.75rem 1rem .75rem 3.25rem; position:relative; border-left:2px solid #e2e8f0; margin-bottom:.75rem; }
.vi-step-list li::before { content:counter(steps); position:absolute; left:-1.1rem; top:.65rem; background:#7c3aed; color:#fff; font-size:.8rem; font-weight:700; width:1.75rem; height:1.75rem; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.vi-cta-mid { background:linear-gradient(135deg,#6d28d9,#7c3aed); color:#fff; border-radius:12px; padding:1.75rem 2rem; margin:2.5rem 0; text-align:center; }
.vi-cta-mid h3 { color:#fff; font-size:1.2rem; font-weight:700; margin:0 0 .5rem; }
.vi-cta-mid p { color:#ede9fe; font-size:.95rem; margin:.5rem 0 1.25rem; }
.vi-cta-mid a { display:inline-block; background:#fff; color:#6d28d9; font-weight:700; font-size:.95rem; padding:.7rem 1.75rem; border-radius:8px; text-decoration:none; }
</style>
```

---

## Passo 3 — Publicar como rascunho via API WP

```python
import os, requests
try:
    from dotenv import load_dotenv
    load_dotenv()  # carrega o .env se python-dotenv estiver instalado
except ImportError:
    pass  # sem o pacote, usa as variáveis já exportadas no ambiente

WP = os.environ.get("WP_URL", "https://seusite.com")
AUTH = (os.environ["WP_USER"], os.environ["WP_APP_PASSWORD"])

# 1. Salvar HTML em arquivo temporário e ler
with open('post_temp.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Criar post como rascunho
r = requests.post(f'{WP}/wp-json/wp/v2/posts', auth=AUTH, json={
    'title': '<TÍTULO DO ARTIGO>',
    'content': content,
    'slug': '<slug-do-artigo>',
    'status': 'draft',
    'categories': [<ID_CATEGORIA>]
})
post_id = r.json()['id']
print('Post ID:', post_id)
```

Sempre criar como **rascunho** (`status: draft`) — o usuário revisa antes de publicar.

---

## Passo 4 — Rank Math via API

```python
# Focus keyword: 2-4 palavras, aparece no título e slug
# Meta description: 140-160 chars, keyword no início, termina com ano

r = requests.post(f'{WP}/wp-json/rankmath/v1/updateMeta', auth=AUTH, json={
    'objectType': 'post',
    'objectID': post_id,
    'meta': {
        'rank_math_focus_keyword': '<keyword 2-4 palavras>',
        'rank_math_description': '<keyword> + o que o artigo cobre + ferramentas + ano. Máx 160 chars.',
        'rank_math_title': '<Título WP otimizado — máx 60 chars>'
    }
})
print('Rank Math:', r.status_code, r.json())
# Esperado: 200 {"slug": true, "schemas": []}
```

Ver a skill `rankmath-seo` para o detalhe de como escolher keyword e escrever a meta description.

---

## Passo 5 — Capa com cover-image

Passe o `post_id` do Passo 3: o script gera a capa, faz o upload e já define a featured image no post — sem etapa manual.

O caminho abaixo assume a raiz do repo clonado; se instalou as skills em `~/.claude/skills/`, ajuste para `~/.claude/skills/cover-image/scripts/gerar_capa.py`.

```bash
python "skills/cover-image/scripts/gerar_capa.py" \
  --post-id <post_id do Passo 3> \
  --query "<query Unsplash específica e visual>" \
  --pill "<Categoria>"
```

O arquivo local é salvo como `cover-<slug>.jpg` (derivado do título). Use `--no-upload` se quiser só gerar o JPG localmente, sem subir no WP.

**Escolha da query:** descrever foto real e específica, não abstrata. Ver a skill `cover-image` para o raciocínio completo.

---

## Passo 6 — Entregar ao usuário

```
Post ID:    XXXX
Rascunho:   {WP_URL}/wp-admin/post.php?post=XXXX&action=edit
Slug:       /slug-do-artigo/
Keyword:    <focus keyword>
Meta desc:  <meta description>
Capa:       ✅ Media ID XXXX
```

Se você mantém um `llms.txt`, lembrar de adicionar a URL após publicar:
```
- [Título]({WP_URL}/slug/): Descrição curta do artigo
```

---

## Otimizações GEO — checklist

- [ ] Definição "O que é X? É..." nas primeiras 60 palavras
- [ ] Todos os H2s em formato de pergunta
- [ ] Fonte externa com dado específico na seção 1
- [ ] FAQ com 3-4 perguntas antes da conclusão
- [ ] Data de publicação no final ("Publicado em mês de ano.")
- [ ] 3-5 links internos distribuídos no artigo
- [ ] 1+ link externo por seção (fontes, referências)
