---
name: rankmath-seo
description: Otimiza o SEO on-page de um post do WordPress via API nativa do Rank Math — preenche focus keyword e meta description de forma estratégica. Analisa o conteúdo do post, escolhe o keyword certo (curto, aparece naturalmente no texto) e escreve uma meta description otimizada para SERP. Use quando quiser preencher o SEO de um post, definir keyword, escrever meta description, ou otimizar o Rank Math de um artigo do blog.
---

# Rank Math — Keyword + Meta Description

**Objetivo:** preencher focus keyword e meta description do Rank Math de forma otimizada para SEO, usando a API nativa do Rank Math (sem plugin extra).

## Credenciais e API

Credenciais vêm do ambiente (ver `.env.example` na raiz do repo): `WP_URL`, `WP_USER`, `WP_APP_PASSWORD`.

```
Endpoint: POST {WP_URL}/wp-json/rankmath/v1/updateMeta
```

**Payload:**
```json
{
  "objectType": "post",
  "objectID": <ID do post>,
  "meta": {
    "rank_math_focus_keyword": "...",
    "rank_math_description": "...",
    "rank_math_title": "..."  // opcional
  }
}
```

## Fluxo de trabalho

### 1. Obter o post

Se o usuário forneceu o ID (ex: URL do WP Admin `?post=1923`), usa direto.
Se não, pergunte.

```python
import os, re, requests
try:
    from dotenv import load_dotenv
    load_dotenv()  # carrega o .env se python-dotenv estiver instalado
except ImportError:
    pass  # sem o pacote, usa as variáveis já exportadas no ambiente

WP_URL = os.environ.get("WP_URL", "https://seusite.com")
AUTH = (os.environ["WP_USER"], os.environ["WP_APP_PASSWORD"])

r = requests.get(
    f'{WP_URL}/wp-json/wp/v2/posts/{POST_ID}?context=edit',
    auth=AUTH
)
p = r.json()
titulo = p['title']['raw']
excerpt = p['excerpt']['raw']
# Extrai texto limpo do conteúdo
content = p['content']['raw']
texto = re.sub(r'<[^>]+>', ' ', content)
texto = re.sub(r'\s+', ' ', texto).strip()
```

Leia os primeiros 3000 chars do texto limpo para entender o tema, dados e termos mais usados.

### 2. Escolher o focus keyword

**Regra principal:** o keyword deve aparecer **naturalmente e com frequência** no título, URL, texto e headings — não force uma frase longa que não existe no conteúdo.

**Como escolher:**
- Prefira frases de 2–4 palavras que o Google mostraria para quem busca esse conteúdo
- Verifique se o termo aparece no título do post e no slug/URL
- Evite frases longas com 5+ palavras — o Rank Math exige match exato e a nota cai
- Se o artigo tem número no título (ex: "55+ estatísticas"), inclua o tema principal sem o número no keyword

**Exemplos de bons keywords:**
- `ia em anuncios pagos` (não `estatísticas ia em anúncios pagos`)
- `chatgpt para marketing` (não `como usar chatgpt para marketing digital 2025`)
- `meta ads com ia` (não `como usar inteligência artificial no meta ads`)

### 3. Escrever a meta description

**Regras:**
- Entre 140–160 caracteres (conta espaços)
- Começa com dado ou número se o artigo tiver (ex: "55+", "47", "26,4%")
- Menciona plataformas/ferramentas específicas que aparecem no conteúdo (Google, Meta, n8n, etc.)
- Termina com o ano ou "para 2026" — sinaliza conteúdo atualizado
- Inclui o keyword naturalmente dentro da frase
- Não usa clickbait genérico ("descubra tudo sobre...") — seja específico

**Estrutura modelo:**
`[Dado/número] + [o que o artigo cobre] + [plataformas/ferramentas] + [ano]`

**Exemplos:**
- `55+ estatísticas sobre IA em anúncios pagos: ROI do Meta Advantage+, Google Performance Max, criativos com IA, segmentação e tendências para 2026.`
- `47 estatísticas de ROI da IA no marketing: produtividade, redução de custos, adoção por setor e o que esperar em 2026.`

### 4. Atualizar via API do Rank Math

```python
import os, requests
try:
    from dotenv import load_dotenv
    load_dotenv()  # carrega o .env se python-dotenv estiver instalado
except ImportError:
    pass  # sem o pacote, usa as variáveis já exportadas no ambiente

WP_URL = os.environ.get("WP_URL", "https://seusite.com")
AUTH = (os.environ["WP_USER"], os.environ["WP_APP_PASSWORD"])

r = requests.post(
    f'{WP_URL}/wp-json/rankmath/v1/updateMeta',
    auth=AUTH,
    json={
        'objectType': 'post',
        'objectID': POST_ID,
        'meta': {
            'rank_math_focus_keyword': keyword,
            'rank_math_description': meta_description,
        }
    }
)
print(r.status_code, r.json())
# Esperado: 200 {"slug": true, "schemas": []}
```

### 5. Confirmar com o usuário

Após salvar, mostre o que foi preenchido:
- **Focus keyword:** `...`
- **Meta description:** `...` (X chars)

Avise que o usuário pode confirmar abrindo o post no WP Admin — os campos vão estar preenchidos no painel do Rank Math. Se quiser mudar qualquer campo, é só pedir.

## Observações importantes

- A API `/rankmath/v1/updateMeta` é nativa do Rank Math — não precisa de plugin adicional
- Os campos são bidirecionais: editar pelo painel do WP ou via API tem o mesmo efeito
- Se o usuário reclamar que a nota do Rank Math está baixa, o problema geralmente é o keyword longo — sugira um mais curto
