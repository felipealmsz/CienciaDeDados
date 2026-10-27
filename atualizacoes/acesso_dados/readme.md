
# Módulo de acesso a dados

Este módulo será responsável por obter os dados necessários para analisar os ativos selecionados pelo usuário.

## Principais operações

- Receber a fonte de dados definida para a análise.
- Carregar os históricos de preços dos ativos.
- Organizar os dados para as etapas seguintes.
- Informar falhas na leitura ou no acesso aos dados.

## Dados de entrada e saída

**Entrada:** arquivo ou fonte de dados contendo os históricos de preços dos ativos.

**Saída:** dados brutos disponibilizados para o módulo de limpeza.

## Exemplo

O módulo recebe um arquivo com os preços históricos de três ativos e disponibiliza essas informações para serem verificadas e preparadas.

## Decisões pendentes

Definir os formatos de arquivo aceitos e se será utilizada alguma API externa.

A implementação será realizada posteriormente.
