# Arquitetura do sistema

## Organização dos módulos

O sistema será dividido em cinco módulos:

- **Domínio (`dominio/`):** representa os elementos do problema, como ativos e carteiras.
- **Acesso a dados (`acesso_dados/`):** carrega dados de arquivos ou de fontes externas.
- **Limpeza (`limpeza/`):** verifica e prepara os dados para análise.
- **Processamento científico (`processamento_cientifico/`):** realiza os cálculos de retorno, risco e fronteira eficiente.
- **Pipeline (`pipeline/`):** coordena a execução das etapas.

## Fluxo de funcionamento

Os dados são carregados, validados e preparados. Depois, o módulo científico realiza os cálculos, e o pipeline reúne os resultados para apresentação.

## Exemplo de estrutura em Python


class PipelineAnalise:
    def executar(self, fonte_dados):
        dados = fonte_dados.carregar()
        dados_limpos = limpar_dados(dados)
        resultados = analisar_carteiras(dados_limpos)
        return resultados


O exemplo ilustra a comunicação entre módulos; as funções ainda serão definidas antes da implementação.


