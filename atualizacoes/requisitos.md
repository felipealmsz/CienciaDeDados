# Documento de requisitos
### Autor: Luís
### Data: 24/11/2026
### Versão: 0.0.1
<!-- comentário  -->


## Introdução e visão geral do sistema

Este é um documento de requisitos para armazenar os dados de uma agenda de telefones e endereços de uma pessoa. O objetivo da agenda telefônica é facilitar o controle dos contatos da pessoa.

## Dados

Deverão ser armazenados dados de nomes dos contantos da pessoa, bem como seus respectivos endereços,e-mail e telefones tal como descritos a seguir:

**contato** - pronome,nome do meio, sobrenome
**endereço** - logradouro, nome do logradouro,número, complemento, CEP, municipalidade, estado/província (pode ficar em branco), país
**e-mail** - tem q conter o caracter @
**telefone** - código numérico de país, código númerico de área, número de telefone~

Note que uma pessoa pode ter mais de um endereço,e-mail e telefone. Além disso, pode compartilhar estes dados com outra pessoa, posto que pode haver pessoas que moram juntas ou compartilham o mesmo telefone.
## Operações com os dados

As operações a seguir podem ser reaizadas com todos os dados:

- Inclusão
- Consulta
- Atualização
- Remoção