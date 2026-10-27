# Módulo de domínio

Este módulo representa os principais elementos do modelo de Markowitz. Ele define como os ativos, as carteiras e os resultados serão organizados no sistema.

## Classes previstas

- **Ativo:** representa um ativo financeiro e armazena suas informações e histórico de preços.
- **Carteira:** reúne os ativos selecionados e seus respectivos pesos.
- **ResultadoCarteira:** armazena o retorno esperado e o risco calculado para uma carteira.
- **AnaliseCarteiras:** reúne os resultados das diferentes carteiras avaliadas.

## Regras do modelo

As carteiras deverão respeitar as regras definidas no projeto: a soma dos pesos deve ser igual a 1 e não serão permitidos pesos negativos.

## Relação com os demais módulos

Este módulo organiza os conceitos utilizados pelo sistema. O acesso aos dados ficará em `acesso_dados/`, e os cálculos serão realizados em `processamento_cientifico/`.

As classes serão implementadas posteriormente.
