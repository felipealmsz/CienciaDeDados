# Módulo de processamento científico

Este módulo será responsável pelos cálculos matemáticos e estatísticos utilizados na análise de carteiras pelo modelo de Markowitz.

## Principais operações

- Calcular os retornos históricos e os retornos esperados dos ativos.
- Calcular a variância e a matriz de covariância dos retornos.
- Gerar diferentes combinações de pesos para as carteiras.
- Calcular o retorno esperado e o risco de cada carteira.
- Identificar as carteiras pertencentes à fronteira eficiente.

## Regras de alocação

As carteiras deverão respeitar as seguintes condições:

- A soma dos pesos dos ativos deve ser igual a 1.
- Os pesos não podem ser negativos, pois não serão permitidas vendas a descoberto.
- A análise deverá considerar até 30 ativos simultaneamente.

## Tecnologia

Os cálculos serão desenvolvidos em Python, utilizando a API RDD do Apache Spark para as operações de processamento de dados. O desenvolvimento e os testes serão realizados no JupyterLab.

## Dados de entrada e saída

**Entrada:** dados preparados, retornos dos ativos e pesos das carteiras.

**Saída:** resultados de risco e retorno, pesos utilizados e identificação da fronteira eficiente.

A implementação e a escolha dos algoritmos serão definidas posteriormente.
