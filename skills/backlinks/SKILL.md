---
name: backlinks
description: Cria artigos de estatísticas data-driven projetados para atrair backlinks e citações de LLMs (ChatGPT, Perplexity, Google AI Overviews). Pesquisa dados de fontes primárias, organiza em seções temáticas com tabelas, e entrega o conteúdo em HTML pronto para publicar via WP API. Use quando quiser criar um artigo de estatísticas, roundup de dados, ou conteúdo do tipo "X+ estatísticas sobre [tema]".
---

# Backlinks — Artigos de Estatísticas Citáveis

> Skill de produção do viniensina.com.br. Os pedaços específicos do site (classes `.vi-*`, shortcode `[vini_cta]`, slugs internos) estão sinalizados — **troque pelo seu setup**.

**Objetivo:** criar o artigo mais citado sobre o tema — outros blogs e IAs (ChatGPT, Perplexity, Google AI Overviews) devem referenciar os dados daqui.

## Contexto do projeto

- **Idioma:** PT-BR (ajuste ao seu)
- **CTA do artigo:** sua oferta. No viniensina é um ebook via shortcode `[vini_cta offer="..." context="..."]` — **não hardcodar link**.
- **Posts internos para linkar (usar 3–5 no artigo, onde contextualmente relevante):**
  - Priorize **outros posts estatísticos irmãos** + os pilares do cluster do tópico.
  - ⚠️ **Confirmar o slug ao vivo antes de linkar** (`curl -s -o /dev/null -w "%{http_code}"`). Link quebrado derruba a citação.

## Passo 1 — Coletar inputs

Perguntar ao usuário se não foram fornecidos:
1. **Tópico** — ex: "IA em anúncios pagos"
2. **Ano** — ex: 2025 ou 2025/2026
3. **Ângulo** (opcional) — ex: "foco em ROI e performance"
4. **Hub** (opcional) — slug do hub ao qual este artigo é satélite

---

## Passo 1.5 — Análise SERP (antes de pesquisar dados)

Buscar no Google pela keyword-alvo: `"[tópico] estatísticas [ano]"` e variações.

**Extrair dos top 5 resultados:**
- Título + H1
- Lista completa de H2s (e H3s relevantes)
- Word count aproximado
- Formato (listicle, roundup, definitional, comparison)
- Presença de: tabela comparativa, FAQ, snippet direto na intro, vídeo, CTA, schema
- H2s que aparecem em 3+ dos top 5 → **seções obrigatórias no artigo**
- Word count mediano → usar como target mínimo

**Identificar o ângulo 10x:**
O que todos os top 5 cobrem mal ou ignoram que o leitor realmente quer? Exemplos:
- Dados do seu país quando todos os resultados são em inglês
- Comparativo de preços quando ninguém traz tabela atualizada
- Dados de fonte primária quando todos citam blogs citando blogs
- Recorte por setor/porte de empresa quando todos falam de "empresas em geral"

Incorporar o ângulo 10x como seção ou destaque diferenciado no artigo.

---

## Passo 2 — Pesquisa (8–15 buscas, antes de escrever qualquer linha)

**Tier 1 — obrigatório 60%+:** HubSpot, McKinsey, Gartner, IDC, Meta earnings, Google, IAB/PwC, Grand View Research, órgãos governamentais, papers acadêmicos.

**Tier 2 — usar com critério:** Statista, eMarketer, Nielsen. Rastrear sempre até a fonte original.

**Tier 3 — proibido:** blogs citando blogs, stats sem metodologia rastreável.

Buscas a realizar (adaptar ao tópico):
- `"[tópico] statistics [ano]"`, `"[tópico] market size [ano]"`, `"[tópico] adoption report [ano]"`
- `"[tópico] ROI statistics [ano]"`, `"[tópico] performance data [ano]"`
- `"[tópico] [plataforma] results [ano]"` (ex: Meta, Google, TikTok)
- `"[tópico] challenges barriers [ano]"`, `"[tópico] forecast [ano+1]"`

Coletar 60–80 stats brutas → filtrar para 40–55 verificadas.

**Resumo de pesquisa (apresentar ao usuário antes de escrever):**
```
Keyword-alvo: "[tópico] estatísticas [ano]"
Stats: [N brutas → N mantidas] | Fontes: [N Tier 1, N Tier 2]
Top 5 stats de maior impacto: ...
Seções planejadas (5–7): [tema — N stats — justificativa]
Links internos mapeados: [3–5 slugs → seções]
Alertas de dados antigos: [temas com dado > 2 anos]
```

---

## Passo 3 — Output: HTML enxuto para WordPress

**Regra de ouro:** o conteúdo é **HTML puro e direto** — **sem `<!-- wp:html -->`**, **sem blocos Gutenberg** (`wp:paragraph`, `wp:heading`, `wp:table`) e **sem `<style>` inline**. No viniensina, as classes `.vi-*` são **globais no tema**: basta usar a classe. Adapte à convenção do seu tema.

**Classes usadas (exemplo viniensina — troque pelas suas):**
- `vi-highlights` — caixa de "principais descobertas" (um `<ul>` dentro, sem `<h3>`)
- `vi-insight` — caixa de insight ao fim de cada seção
- `vi-table-note` — nota de "leitura rápida" logo antes de uma tabela

**Demais elementos são HTML nu:**
- Tabelas: `<table>` com `<thead>`/`<tbody>` e `<th scope="col">` — **sem wrapper e sem classe**
- Títulos de seção: `<h2>` puro — **sem classe**
- Parágrafos: `<p>` puro
- CTA: shortcode da sua oferta — **nunca** um `<div>` com link hardcoded

O tema injeta sozinho: featured image, H1, meta (autor/data), sidebar, posts relacionados — **não incluir nada disso**. Proibido `body{}`, `:root{}`, `<style>`, `.wp-block-*`, DOCTYPE/html/head/body.

### Estrutura obrigatória (nesta ordem)

```html
<p>[Abertura: 2–3 frases situando o tema. Direto, sem enrolação.]</p>
<p>[Parágrafo-âncora: <strong>o dado que resume o cenário</strong>, com fonte e ano. É o trecho que a IA tende a citar — capriche.]</p>
<p>Este levantamento reúne <strong>[N] estatísticas verificáveis</strong> sobre [subtemas]. [Frase curta posicionando como página citável.]</p>

<h2>Resposta rápida: [pergunta-chave do tópico]?</h2>
<p>Se você precisa citar poucos números, estes são os mais fortes:</p>
<table>
  <thead><tr><th scope="col">Dado</th><th scope="col">Valor</th><th scope="col">Fonte</th></tr></thead>
  <tbody>
    <tr><td>[métrica]</td><td>[valor]</td><td>[Organização, Ano]</td></tr>
    [6–8 linhas de maior impacto]
  </tbody>
</table>
<div class="vi-insight"><strong>Insight:</strong> [a leitura de uma frase que resume o tópico].</div>

<div class="vi-highlights">
  <ul>
    <li><strong>[Descoberta curta:]</strong> [dado + fonte].</li>
    [5–8 bullets, do mais impactante ao menos esperado]
  </ul>
</div>

<h2>Como citar este levantamento</h2>
<p>Se você usar estes dados em artigo, relatório, apresentação ou material comercial, cite assim:</p>
<p>&gt; [Seu site]. "[Título do levantamento]". Coleta e curadoria de fontes públicas, [ano].</p>
<p>Quando citar um número específico, prefira mencionar também a fonte original. Exemplo: "Segundo [Fonte], citada por [seu site], [dado]."</p>

[REPETIR PARA CADA SEÇÃO TEMÁTICA — 5 a 7 vezes:]
<h2>[Título da seção]</h2>
<p>[Parágrafo interpretativo: o que os dados revelam e por que importam. Não antecipar o que a tabela mostra.]</p>
<p class="vi-table-note">Leitura rápida: [1 frase orientando a tabela abaixo].</p>
<table>
  <thead><tr><th scope="col">Estatística</th><th scope="col">Valor</th><th scope="col">Fonte</th></tr></thead>
  <tbody>
    <tr><td>[dado]</td><td>[valor]</td><td>[Organização — Relatório, Ano]</td></tr>
    [4–8 linhas]
  </tbody>
</table>
<div class="vi-insight"><strong>Insight:</strong> [implicação prática. Pode incluir 1 link interno contextual aqui: <a href="/slug/">texto</a>.]</div>

[CTA — inserir UMA vez, após a 3ª ou 4ª seção, como shortcode da sua oferta]

<h2>[Tópico] em números: tabela completa</h2>
<p>Consolidação das principais métricas do artigo para consulta e citação rápida.</p>
<table>
  <thead><tr><th scope="col">Estatística</th><th scope="col">Valor</th><th scope="col">Fonte</th></tr></thead>
  <tbody>[15–20 stats mais impactantes]</tbody>
</table>

<h2>O que os dados significam para [público — ex: pequenas empresas]</h2>
<p>[Aplicação prática dos dados para o leitor do site.]</p>

<h2>Perguntas frequentes</h2>
<h3>[pergunta]</h3>
<p>[resposta com dado do artigo]</p>
[5–6 pares. SEMPRE aqui — antes de Metodologia, nunca depois.]

<h2>Metodologia</h2>
<p>As estatísticas foram coletadas em [mês/ano], priorizando fontes primárias com metodologia declarada. Dados sem fonte rastreável foram descartados. Nenhuma estatística foi inventada ou arredondada para dramatizar. Página revisada trimestralmente.</p>

<h2>Fontes consultadas</h2>
<ul>
  <li><a href="[url]" target="_blank" rel="noopener">[Organização — Nome do Relatório, Ano]</a></li>
  [uma linha por fonte]
</ul>
<p><em>Última atualização: [mês de ano]. Para citar este relatório: [seu site]/[slug]/</em></p>
```

> **Ordem verificada em produção:** "Resposta rápida" é o **1º bloco do artigo**, antes até do `vi-highlights`. E a **FAQ vem antes de Metodologia/Fontes**, nunca depois. Escrever já nessa ordem desde o rascunho.

> A **FAQ visível** já vai no corpo desde o rascunho. O **FAQPage JSON-LD** deve ser anexado por um passo separado do seu pipeline, que EXIGE a FAQ visível presente e só acrescenta o `<script>`. Nunca colar o schema à mão.

> ⚠️ **Guard de idempotência:** se o seu script de schema pula a aplicação ao achar a string `FAQPage` no conteúdo, cuidado — um artigo que **menciona "FAQPage" no texto visível** (comum em posts de SEO/GEO) engana o guard e o schema nunca é aplicado. Checar a contagem de `FAQPage` no conteúdo bruto antes e depois.

> ⚠️ **H1 fantasma:** blocos de código com `#` no início da linha (ex: exemplos de Markdown) viram `<h1>` no WordPress e quebram o QA de "1 H1". Evitar code fence com `#`; usar tabela ou `<code>` inline.

> **Os 3 blocos de citação em IA são INEGOCIÁVEIS — mesmo em satélites/explicadores:** (1) **"Resposta rápida"** (tabela de resposta direta), (2) **"Como citar este [levantamento/guia]"**, (3) **FAQ + FAQPage**. São eles que fazem ChatGPT/Perplexity/AI Overview citarem e atribuírem a página — independente do formato.

---

## Regras de escrita

- Começar com número: "94% dos marketers..." (não "A maioria...")
- Insight ≠ repetição da tabela — interpreta o que o dado *significa*
- Parágrafos curtos (1–4 frases) | Bold no stat mais impactante de cada seção
- Citação inline: `Dado (Organização, Nome do Relatório Ano)`
- **Proibido:** delve, game-changer, leverage, unlock, alavancar, navegar pelas complexidades, no cenário atual, vale ressaltar, em um mundo onde, quando se trata de, revolucionar
- Nunca inventar stat; nunca arredondar para dramatizar

---

## Passo 4 — Metadados para publicação

```
Título WP:       [título completo com número de stats e ângulos]
Slug:            /estatisticas-[topico]-[ano]/
Excerpt:         [1–2 frases com dado principal + fontes — máx 160 chars]
Categoria:       [ID da categoria WP do seu site]
Tags:            [5 slugs]
Meta desc RM:    [até 160 chars com keyword-alvo no início]
Focus keyword:   [keyword-alvo principal]
```

---

## Passo 5 — Plano de cluster (sempre ao final)

Analisar seções com potencial para artigo satélite (6+ stats próprias, keyword buscável distinta, ângulo não canibaliza o hub):

```
Título: [título do satélite]
Slug: /estatisticas-[recorte]/
Ângulo: [o que diferencia do hub]
Stats reutilizáveis do hub: [3–5]
O que ainda precisa buscar: [lacuna]
Linka de volta para: [slug do hub]
```

---

## Passo 6 — Publicação

A skill entrega o conteúdo; a publicação segue o pipeline do seu blog:

1. **Rascunho via WP API:** `POST /wp/v2/posts` com `status=draft`, `content` = HTML puro (Passo 3), `slug`, `title`, `excerpt`, `categories`. Sempre `context=edit` e ler/gravar `content` como `raw` (nunca `content.rendered`).
2. **Capa:** use a skill `cover-image`.
3. **FAQ + schema:** a FAQ visível já vem do rascunho (antes de Metodologia). Anexe o FAQPage JSON-LD por um passo separado; ele EXIGE a FAQ visível e só acrescenta o `<script>`.
4. **Acentuação:** após publicar, checar o corpo e a meta description por acentos comidos (bug recorrente de encoding em algumas APIs). Conferir também se sobrou link markdown cru `[texto](url)` no HTML.
5. **Rank Math:** use a skill `rankmath-seo`.
6. **IndexNow:** envie a URL via IndexNow (Bing/Yandex) para acelerar a reindexação.

> Regra dura: post no WP = **conteúdo apenas**. Nunca DOCTYPE/html/head/body, nunca `<style>` global, nunca CSS de tema.

---

## Checklist antes de entregar

- [ ] 5–7 seções temáticas
- [ ] "Resposta rápida" é o 1º bloco (antes do `vi-highlights`) + "Como citar este levantamento"
- [ ] FAQ visível posicionada ANTES de Metodologia/Fontes
- [ ] 40–55 stats únicas
- [ ] 60%+ fontes Tier 1
- [ ] Nenhuma stat sem fonte rastreável
- [ ] 3–5 links internos no total (não um por seção), **slug confirmado ao vivo**
- [ ] 1+ link externo por seção
- [ ] Insight ≠ repetição da tabela
- [ ] CTA como shortcode (não link hardcoded)
- [ ] Formato: HTML puro, sem `<style>` e sem `<!-- wp:html -->`
- [ ] Metadados de publicação fornecidos (incluindo focus keyword)
- [ ] Plano de cluster entregue
