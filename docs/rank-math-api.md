# Rank Math API Notes

Notas práticas para atualizar campos de SEO on-page do Rank Math via REST API nativa.

## Endpoint

```text
POST /wp-json/rankmath/v1/updateMeta
```

Exemplo com Python:

```python
import os
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

WP_URL = os.environ.get("WP_URL", "https://seusite.com")
AUTH = (os.environ["WP_USER"], os.environ["WP_APP_PASSWORD"])

r = requests.post(
    f"{WP_URL}/wp-json/rankmath/v1/updateMeta",
    auth=AUTH,
    json={
        "objectType": "post",
        "objectID": 1234,
        "meta": {
            "rank_math_focus_keyword": "claude code skills",
            "rank_math_description": "Claude Code Skills para SEO/GEO: veja um workflow real com WordPress, conteúdo citável, capas e Rank Math.",
            "rank_math_title": "Claude Code Skills para SEO/GEO",
        },
    },
    timeout=30,
)
r.raise_for_status()
print(r.json())
```

Resposta comum:

```json
{
  "slug": true,
  "schemas": []
}
```

## Campos úteis

| Campo | Uso |
|---|---|
| `rank_math_focus_keyword` | Keyword principal do post |
| `rank_math_description` | Meta description |
| `rank_math_title` | Título SEO |

## Como escolher focus keyword

- Use 2-4 palavras.
- Prefira termo que aparece no título e slug.
- Evite frases longas.
- Não inclua ano se o termo principal não depende do ano.
- Não force match exato estranho só para "ganhar nota".

## Como escrever meta description

Boa meta description:

- tem 140-160 caracteres;
- começa com o valor principal quando possível;
- inclui a keyword naturalmente;
- menciona ferramentas, público ou recorte;
- termina com ano quando atualização importa;
- não usa clickbait genérico.

Modelo:

```text
[Keyword/tema]: [o que o artigo entrega] com [ferramentas/recorte] para [público/contexto] em [ano].
```

## Erros comuns

- Usar email em `WP_USER` quando o login do WordPress é outro.
- Usar senha normal em vez de Application Password.
- Atualizar post publicado sem backup.
- Regravar `content.rendered` em vez de `content.raw`.
- Usar keyword longa demais.
- Escrever meta description que não corresponde ao artigo.

## Segurança

- Nunca commite `.env`.
- Nunca cole Application Password real em README, issue ou commit.
- Use `.env.example` só com placeholders.
- Revogue a Application Password se ela aparecer em log ou histórico público.

