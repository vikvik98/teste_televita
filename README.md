# Teste para a vaga de back-end na Televita.

Projeto de modelagem de dados e criação de uma API utilizando Python e Flask.

**Este projeto é parte do processo de seleção de desenvolvedor backend da [Telavita](https://telavita.com.br).**

## Sobre o projeto

A ACMEVita está expandindo seus negócios e precisa de um sistema para gerenciar seus departamentos, colaboradores e dependentes.

O seu único desenvolvedor backend está de ferias, você foi recrutado para finalizar este projeto, boa sorte!

### Requisitos

#### Como um Usuário da API eu gostaria de consultar todos os departamentos para visualizar a organização da ACMEVita.

  * Cada departamento deve possuir um *nome do departamento*.
  * A API deve responder com uma listagem de departamentos no formato JSON informando o *nome do departamento* de cada departamento.

#### Como um Usuário da API eu gostaria de consultar todos os colaboradores de um departamento para visualizar a organização da ACMEVita.

  * Cada colaborador deve possuir um *nome completo*.
  * Cada colaborador deve pertencer a *um* departamento.
  * Cada colaborador pode possuir *nenhum, um ou mais* dependententes.
  * A API deve responder com uma listagem de colaboradores do departamento no formato JSON informando o *nome completo* de cada colaborador e a respectiva flag booleana `have_dependents` caso o colaborador possua *um ou mais dependentes*.


## Instalando projeto

* Faça um clone do projeto.
* Crie uma env.
* Rodo o comando pip install -r requirements.txt para instalar as bibliotecas.
* Dentro da pasta src rode o comando python app.py

## Endpoints

* */departments/* para visualizar e criar departamentos.
* */departments/department_id/* para visualizar, editar e deletar um departamento especifico.
* */collaborator/* para visualizar e criar colaboradores.
* */collaborator/collaborator_id/* para visualizar, editar e deletar um colaborador especifico.
* */collaborator/collaborator_id/dependents/dependent_id/* para tornar um colaborador dependente do outro.

## Exemplo de estrutura de json para os POSTs

# Post para departamentos
{
   "id": 1,
   "name": "Department 1"
}

# Post para colaboradores

{
   "id": 3,
   "name": "Collaborator 3",
   "department_id": 1
}
