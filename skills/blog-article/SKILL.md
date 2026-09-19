---
name: blog-article
description: Cria um novo artigo para WordPress com pesquisa, HTML limpo, links internos, metadados e rascunho seguro. Use para produzir posts novos. Para auditar ou atualizar uma URL existente, use content-refresh.
---

# Blog Article — novo artigo para WordPress

Crie conteúdo útil, verificável e pronto para revisão. Esta é uma versão sanitizada do fluxo do viniensina.com.br; adapte tema, classes, CTA, categorias e links ao site do usuário.

## Limites

- Não publique ao vivo sem autorização explícita. O padrão é entregar o HTML ou criar `status: draft`.
- Não invente dados, experiência própria, testes, depoimentos ou resultados.
- Não force tamanho, densidade de keyword, FAQ, tabela ou schema quando não ajudarem o leitor.
- Não trate uma estrutura de texto como garantia de ranking ou citação por IA.
- Para uma página já publicada, use `content-refresh` e preserve a janela de medição.

## Entradas

Use o que o usuário já forneceu. Pergunte apenas pelo que bloquear a execução:

- tópico e intenção principal;
- público e resultado esperado;
- URL/slug planejado e cluster, se já existirem;
- site ou categoria WordPress, se a criação do rascunho foi solicitada;
- CTA/oferta e restrições editoriais.

Se não houver keyword, derive uma hipótese da intenção e valide com dados disponíveis. GSC é útil para demanda já observada; SERP e ferramentas externas são sinais auxiliares, não verdade absoluta.

## Pesquisa e brief

Antes de escrever:

1. Identifique a pergunta principal e as tarefas secundárias do leitor.
2. Revise resultados atuais e fontes primárias quando o tema puder ter mudado.
3. Separe fatos verificáveis, interpretação editorial e exemplos hipotéticos.
4. Mapeie de 2 a 5 links internos realmente contextuais e confirme os destinos.
5. Defina o diferencial: dado próprio, teste, comparação, template, experiência ou síntese original.

Não replique a estrutura dos concorrentes mecanicamente. Use a pesquisa para descobrir lacunas e produzir conteúdo não comoditizado.

## Redação

- Responda à intenção no primeiro bloco útil.
- Use títulos descritivos; perguntas são opcionais, não obrigatórias.
- Explique termos antes de siglas e diferencie fato, estimativa e opinião.
- Dê a cada dado uma fonte rastreável e um período.
- Prefira exemplos completos a listas superficiais.
- Use tabelas apenas quando facilitarem comparação.
- Faça a profundidade seguir a complexidade do tema; não existe contagem ideal de palavras.
- Evite promessas absolutas, estatísticas sem fonte e linguagem inflada.

FAQ é opcional. Inclua apenas perguntas que complementem a página sem duplicar o corpo. Desde maio de 2026, o Google não exibe rich results de FAQ; não use `FAQPage` como argumento de ganho de SERP.

## Formato para WordPress

Entregue o conteúdo no formato esperado pelo site. No fluxo de referência:

- HTML sem `DOCTYPE`, `<html>`, `<head>` ou `<body>`;
- sem `<style>` global ou CSS de tema dentro do post;
- sem H1 quando o tema já injeta o título;
- sem Markdown cru misturado ao HTML;
- tabelas com `<thead>`, `<tbody>` e `<th scope="col">`;
- classes visuais e shortcode de CTA configuráveis, nunca assumidos como universais.

Leia e grave `content.raw` com `context=edit`; não use `content.rendered` como fonte para sobrescrever um post.

## Metadados

Forneça título editorial, slug estável, excerpt/meta description fiel, focus keyword apenas quando o site usa esse campo, categoria, links internos e fontes. Use `rankmath-seo` quando o usuário pedir atualização via API.

## Rascunho e mídia

Quando autorizado a escrever no WordPress:

1. Crie o post como `draft`.
2. Confirme ID, slug e URL de edição retornados pela API.
3. Gere a capa com `cover-image` somente se solicitada ou incluída no escopo.
4. Atualize Rank Math somente com valores revisados.
5. Mostre o rascunho ao usuário antes de qualquer publicação ao vivo.

## QA

- [ ] fatos sensíveis ou atuais têm fonte primária e data;
- [ ] nenhum número foi inventado ou dramatizado;
- [ ] intenção principal respondida cedo;
- [ ] links internos e externos apontam ao destino correto;
- [ ] CTA corresponde à oferta e não interrompe a resposta;
- [ ] HTML não contém H1 duplicado, CSS global ou Markdown cru;
- [ ] title, slug, canonical esperado e meta são consistentes;
- [ ] leitura mobile foi considerada para tabelas, imagens e blocos longos;
- [ ] ações externas executadas e pendentes estão separadas no resumo.

## Entrega

Informe o que foi criado, as fontes principais, as decisões editoriais, o local do rascunho/arquivo e qualquer etapa que dependa de revisão humana. Não apresente publicação, indexação ou desempenho futuro como concluídos sem evidência.
