---
name: content-refresh
description: Audita e atualiza um artigo existente com dados de Search Console, checagem factual, SERP e QA WordPress. Use para refresh, queda de tráfego, CTR baixo, conteúdo desatualizado ou revisão editorial. Não use para criar um post novo.
---

# Content Refresh — atualização de conteúdo existente

Melhore uma URL publicada com a menor mudança capaz de resolver o problema demonstrado. Preserve histórico, conversão e capacidade de medir o efeito.

## Limites

- Diagnosticar não autoriza editar. Só altere arquivos, WordPress ou metadados quando o usuário pedir a mudança.
- Não mude slug, intenção, CTA, oferta ou arquitetura sem justificar o impacto.
- Antes de sobrescrever conteúdo ao vivo, obtenha `content.raw` com `context=edit` e faça backup recuperável.
- Não reotimize uma página recém-editada só porque os dados ainda não reagiram. Confirme recrawl e aguarde uma janela adequada.
- GSC mostra associação e desempenho observado; não prova por que uma mudança aconteceu.

## Evidência mínima

Reúna o que estiver disponível:

- URL, conteúdo bruto atual, title, meta, canonical e data da última edição;
- GSC por página e consulta, comparando janelas equivalentes;
- data do último crawl ou inspeção;
- conversões/CTA que não podem ser quebrados;
- fontes oficiais para alegações que mudam com o tempo;
- SERP pública ou ferramenta de terceiros como sinal complementar.

DataForSEO é opcional. Nunca exponha credenciais; leia login e senha de variáveis de ambiente ou `.env` ignorado pelo Git. Registre custo e trate ausência de saldo/dados como limitação, não como licença para inventar volume.

## Diagnóstico

Classifique a oportunidade antes de editar:

| Sinal | Primeira hipótese de ação |
|---|---|
| Muitas impressões, CTR fraco, posição competitiva | Testar title/meta e resposta inicial antes de expandir tudo |
| Posição 8–20 com consultas coerentes | Cobrir lacunas reais, melhorar links internos e resposta à intenção |
| Fato, preço, política ou produto desatualizado | Corrigir imediatamente com fonte primária |
| Intenção mudou ou conteúdo não entrega o prometido | Considerar reconstrução preservando URL e ativos úteis |
| Edição recente sem recrawl ou janela completa | Registrar hold; medir antes de nova intervenção |
| Poucos dados ou consultas incoerentes | Investigar; não reescrever por impulso |

Escolha entre `sem mudança`, `ajuste cirúrgico`, `revisão editorial` ou `reconstrução`. Justifique a menor intervenção suficiente.

## Plano de mudança

Antes de editar, registre problema e janela de dados, hipótese refutável, elementos preservados, mudanças propostas, riscos e data mínima para a próxima leitura.

## Implementação

1. Salve backup do conteúdo bruto e metadados.
2. Faça apenas as mudanças aprovadas.
3. Preserve links, CTA e blocos que funcionam, salvo evidência contrária.
4. Remova duplicação, números frágeis, promessas absolutas e informação obsoleta.
5. Diferencie exemplos hipotéticos de casos reais.
6. Mantenha FAQ apenas quando acrescentar valor; não dependa de `FAQPage` para rich result no Google.
7. Atualize title/meta somente quando continuarem fiéis ao conteúdo.

## QA pós-edição

Valide conteúdo bruto e página pública:

- resposta HTTP e indexabilidade;
- canonical para a URL final;
- exatamente um H1 no documento renderizado;
- title/meta esperados;
- links, imagens, CTA e eventos importantes;
- ausência de schema duplicado, Markdown cru e caracteres corrompidos;
- layout mobile sem overflow global;
- conteúdo principal presente após cache/CDN.

IndexNow pode acelerar descoberta em mecanismos compatíveis, mas não comprova crawl nem indexação.

## Maturação

Registre o momento da edição e confirme recrawl posterior. Compare janelas equivalentes de 7, 14 e 28 dias quando houver volume suficiente. Durante o hold editorial, corrija apenas falhas críticas ou fatos materialmente errados.

## Entrega

Relate diagnóstico e evidências, mudanças aplicadas e preservadas, backup e validações, limitações, estado atual e próxima data ou condição de decisão.
