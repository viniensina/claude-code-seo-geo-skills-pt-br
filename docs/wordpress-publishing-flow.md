# WordPress SEO Publishing Flow

Fluxo seguro para publicar conteúdo de SEO/GEO no WordPress usando REST API, mídia, Rank Math e revisão humana.

O princípio é simples: criar primeiro como rascunho, validar tudo e só depois publicar com autorização. Para páginas existentes, faça backup do conteúdo bruto antes de sobrescrever.

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
- Ler e gravar `content.raw` com `context=edit`; nunca reconstruir um post a partir de `content.rendered`.

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

Publicação ao vivo é uma mudança externa. Só avance quando o usuário tiver pedido a publicação ou aprovado claramente o rascunho.

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
- Conferir a página no mobile e garantir que tabelas não gerem overflow global.
- Conferir CTA, caracteres acentuados e ausência de Markdown cru.
- Enviar IndexNow se o site usa Rank Math/IndexNow.

## 7. Pós-publicação

- Atualizar links internos de posts relacionados.
- Adicionar ao `llms.txt` apenas se você o mantém para serviços que o utilizam. O Google declara que `llms.txt` não ajuda nem prejudica visibilidade ou ranking no Google Search.
- Monitorar Google Search Console.
- Revisar se imagens, CTA e tabelas estão bons no mobile.
- Confirmar recrawl posterior antes de atribuir efeito à publicação.
- Para refreshes, comparar janelas equivalentes e evitar novas mudanças durante a maturação.

