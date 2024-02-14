# API de Gerenciamento de Estacionamento Rotativo

Esta é uma API desenvolvida para a disciplica de Manutenção de software usando Django REST Framework para gerenciar um estacionamento rotativo.

## Rotas

### Reservas

- Listar todas as reservas: `GET /api/reservas/`
- Criar uma reserva: `POST /api/reservas/`
- Ver detalhes de uma reserva específica: `GET /api/reservas/<id>/`
- Atualizar uma reserva específica: `PUT /api/reservas/<id>/`
- Excluir uma reserva específica: `DELETE /api/reservas/<id>/`
- Finalizar uma reserva específica: `POST /api/reservas/<id>/finalizar/`

### Carros

- Listar todos os carros: `GET /api/carros/`
- Criar um carro: `POST /api/carros/`
- Ver detalhes de um carro específico: `GET /api/carros/<id>/`
- Atualizar um carro específico: `PUT /api/carros/<id>/`
- Excluir um carro específico: `DELETE /api/carros/<id>/`

### Vagas

- Listar todas as vagas: `GET /api/vagas/`
- Criar uma vaga: `POST /api/vagas/`
- Ver detalhes de uma vaga específica: `GET /api/vagas/<id>/`
- Atualizar uma vaga específica: `PUT /api/vagas/<id>/`
- Excluir uma vaga específica: `DELETE /api/vagas/<id>/`

## Instalação e Execução

1. Clone o repositório: `git clone https://github.com/seu-usuario/seu-repositorio.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações do banco de dados: `python manage.py migrate`
4. Inicie o servidor de desenvolvimento: `python manage.py runserver`

Certifique-se de ajustar as URLs de acordo com a estrutura do seu projeto.
