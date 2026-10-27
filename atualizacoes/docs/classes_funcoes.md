# Classes e funções

### Classes principais

- **`Ativo`**: representa um ativo financeiro e armazena suas informações e preços históricos.
- **`Carteira`**: organiza os ativos que compõem a carteira e seus respectivos pesos.
- **`ResultadoCarteira`**: armazena os resultados calculados, como retorno esperado e risco.
- **`AnaliseCarteiras`**: reúne os resultados das diferentes carteiras analisadas.

### Funções principais

- **`carregar_dados()`**: obtém os dados de entrada.
- **`validar_dados()`**: verifica se os dados estão completos e adequados para análise.
- **`calcular_retornos()`**: calcula os retornos dos ativos a partir dos preços históricos.
- **`calcular_matriz_covariancia()`**: calcula a covariância entre os retornos dos ativos.
- **`calcular_retorno_carteira()`**: calcula o retorno esperado da carteira considerando os pesos dos ativos.
- **`calcular_risco_carteira()`**: calcula a variância e o risco da carteira.
- **`identificar_fronteira()`**: identifica as carteiras que compõem a fronteira eficiente.
- **`executar_analise()`**: coordena as etapas da análise, desde a obtenção dos dados até a organização dos resultados.
