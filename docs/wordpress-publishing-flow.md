# WordPress SEO Publishing Flow

Fluxo seguro para publicar conteúdo de SEO/GEO no WordPress usando REST API, mídia, Rank Math e revisão humana.

O princípio é simples: criar primeiro como rascunho, validar tudo e só depois publicar.

## 1. Preparar ambiente

Variáveis necessárias:

```dotenv
WP_URL=https://seusite.com
WP_USER=seu-usuario-wp
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx
```

Boas práticas:

- Nunca commitar `.env`.
- Usar Application Password do WordPress, não senha principal.
- Usar usuário com permissão mínima suficiente.
- Validar em rascunho antes de publicar.

## 2. Criar rascunho

Payload mínimo:

```json
{
  "title": "Título do artigo",
  "slug": "slug-do-artigo",
  "status": "draft",
  "content": "<p>HTML do conteúdo</p>",
  "excerpt": "Meta resumo curto",
  "categories": [4]
}
```

Cuidados:

- Criar como `draft`.
- Enviar conteúdo já no formato esperado pelo tema.
- Evitar `DOCTYPE`, `<html>`, `<head>` e `<body>`.
- Não usar conteúdo renderizado como fonte para regravar post; prefira `content.raw`.

## 3. Subir mídia

Endpoint:

```text
POST /wp-json/wp/v2/media
```

Headers típicos:

```text
Authorization: Basic ...
Content-Disposition: attachment; filename="cover.jpg"
Content-Type: image/jpeg
```

Depois do upload:

- Salvar o `media_id`.
- Preencher `alt_text`.
- Usar imagens com largura controlada no HTML.
- Definir `featured_media` no post quando fizer sentido.

## 4. Atualizar Rank Math

Endpoint nativo:

```text
POST /wp-json/rankmath/v1/updateMeta
```

Payload:

```json
{
  "objectType": "post",
  "objectID": 1234,
  "meta": {
    "rank_math_focus_keyword": "keyword principal",
    "rank_math_description": "Meta description com 140-160 caracteres.",
    "rank_math_title": "Título SEO opcional"
  }
}
```

Cuidados:

- Focus keyword deve ter 2-4 palavras.
- Meta description precisa refletir o conteúdo real.
- Não prometer dados que o artigo não entrega.

## 5. QA em rascunho

Antes de publicar:

- [ ] Título e slug corretos.
- [ ] Categoria correta.
- [ ] Featured image definida.
- [ ] Imagens do corpo com `alt`.
- [ ] Links internos funcionando.
- [ ] Links externos abrindo.
- [ ] CTA correto.
- [ ] FAQ visível.
- [ ] Nenhum Markdown cru no HTML.
- [ ] Rank Math preenchido.

## 6. Publicar

Quando o rascunho estiver validado:

```json
{
  "status": "publish"
}
```

Depois da publicação:

- Conferir URL pública.
- Validar canonical.
- Conferir se a página está indexável.
- Conferir H1 único.
- Enviar IndexNow se o site usa Rank Math/IndexNow.

## 7. Pós-publicação

- Atualizar links internos de posts relacionados.
- Adicionar ao `llms.txt`, se você mantém um.
- Monitorar Google Search Console.
- Revisar se imagens, CTA e tabelas estão bons no mobile.

