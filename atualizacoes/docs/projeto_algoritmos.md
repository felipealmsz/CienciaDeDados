# Projeto dos algoritmos

## 1. Preparação dos dados

1. Receber os dados.
2. Verificar formatos, valores ausentes e inconsistências.
3. Preparar os dados para os cálculos.
4. Devolver os dados preparados ou indicar um erro.

## 2. Cálculo dos retornos

1. Receber os preços históricos.
2. Organizar os preços por ativo e período.
3. Calcular o retorno entre períodos consecutivos.
4. Devolver os retornos calculados.

## 3. Cálculo do retorno e do risco

1. Receber os pesos dos ativos e seus retornos.
2. Calcular o retorno esperado da carteira.
3. Calcular a matriz de covariância.
4. Utilizar os pesos e a matriz para calcular a variância da carteira.
5. Obter o risco a partir da variância.
6. Armazenar os resultados.

**Exemplo:** uma carteira com dois ativos terá seu risco calculado considerando tanto o risco individual de cada ativo quanto a covariância entre eles.

## 4. Identificação da fronteira eficiente

1. Receber os resultados das carteiras avaliadas.
2. Comparar o retorno e o risco de cada carteira.
3. Identificar as carteiras que não são dominadas por outras.
4. Devolver as carteiras pertencentes à fronteira eficiente.

## 5. Execução completa

1. Carregar os dados.
2. Validar e preparar os dados.
3. Calcular retornos e covariâncias.
4. Avaliar as carteiras.
5. Identificar a fronteira eficiente.
6. Reunir os resultados para apresentação.

## Pontos a definir

A estratégia para gerar carteiras candidatas, o tratamento de dados ausentes e a aplicação do método RDD serão definidos posteriormente.
