# Módulo de pipeline

Este módulo será responsável por coordenar a execução da análise, conectando os demais módulos na ordem necessária.

## Sequência de execução

1. Receber os ativos e a fonte de dados selecionada.
2. Solicitar o carregamento dos históricos de preços.
3. Encaminhar os dados para validação e limpeza.
4. Enviar os dados preparados ao processamento científico.
5. Coordenar a geração e a avaliação das carteiras.
6. Reunir os resultados e disponibilizá-los para apresentação.

## Resultados esperados

O pipeline deverá organizar os resultados necessários para apresentar:

- Os pesos atribuídos a cada ativo.
- O retorno esperado e o risco das carteiras.
- A identificação das carteiras eficientes.
- Os dados utilizados na tabela e no gráfico de risco e retorno.

## Desempenho e consistência

A execução deverá considerar o limite de 30 ativos e o tempo máximo previsto de 2 segundos para os cálculos e a representação gráfica.

A tabela e o gráfico deverão utilizar a mesma base de resultados.

## Tecnologia

O pipeline será desenvolvido em Python e coordenará as etapas de processamento com Apache Spark RDD, no ambiente JupyterLab.

A implementação será realizada posteriormente.
