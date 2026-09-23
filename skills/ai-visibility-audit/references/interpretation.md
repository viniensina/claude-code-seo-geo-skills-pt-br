# Interpretação dos dados

## Janelas móveis

Se o snapshot A cobre 23/08–20/09 e o B cobre 07/09–05/10, há 14 datas em comum. O delta entre os totais é válido como mudança da janela móvel, mas não representa o que aconteceu apenas nos 15 dias entre as exportações.

Relate sempre:

- início e fim reais de cada snapshot;
- quantidade de datas retornadas;
- dias e percentual de sobreposição;
- se a comparação é móvel ou não sobreposta.

Para Overview, use os dados diários para comparar subperíodos não sobrepostos, como últimos 7 dias versus 7 anteriores. Pages e Grounding queries normalmente chegam agregados para toda a janela e não permitem isolar o trecho exclusivo.

## Linhas ausentes

Em uma comparação por página ou consulta:

- presente nos dois arquivos: delta calculável;
- presente apenas no atual: `not_returned_previous`;
- presente apenas no anterior: `not_returned_current`;
- não substitua nenhum desses estados por zero.

## Totais entre visões

Não force reconciliação entre Overview, Pages e Grounding queries. Preserve cada soma, mostre a diferença e descreva que as visões podem usar amostragem e agregação distintas.

## Cruzamento com GSC e analytics

Normalize a URL e compare sinais, sem somá-los:

- muitas citações + muitas impressões: proteger precisão e atualização;
- muitas impressões + página não retornada no Bing: hipótese de teste, não “zero citações”;
- muitas citações + poucas sessões: oportunidade de investigar conversão e atribuição;
- queda simultânea em fontes diferentes: prioridade de diagnóstico, ainda sem causalidade automática.

GSC, analytics e Bing possuem cobertura, atraso, unidade e população diferentes. Mantenha a janela e a fonte ao lado de cada métrica.

## Linguagem recomendada

Use: “o total da janela móvel aumentou 20%”, “a página não foi retornada no snapshot atual” e “a edição coincide temporalmente com a mudança”.

Evite: “ganhou 200 novas citações”, “caiu para zero” quando a linha sumiu e “a otimização causou o crescimento” sem experimento adequado.

