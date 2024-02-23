# Hotel Reservation API

Bem-vindo ao repositório da Hotel Reservation API! Esta API foi desenvolvida como um exemplo prático para demonstrar a criação e o gerenciamento de reservas de hotel utilizando FastAPI, uma framework moderna e rápida para construir APIs com Python.

## Sumário

- [Sobre a API](#sobre-a-api)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints](#endpoints)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Executando Testes](#executando-testes)
- [Contribuindo](#contribuindo)

## Sobre a API

A Hotel Reservation API permite aos usuários criar e listar reservas de hotel. Cada reserva contém informações como o nome do cliente, o nome do hotel, e as datas de check-in e check-out. As reservas são armazenadas em um arquivo CSV, simplificando a persistência de dados para este exemplo.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construir APIs com Python, oferecendo alta performance e facilidades para documentação automática.
- **Pydantic**: Utilizado para a validação de dados e definição de modelos de dados.
- **Python 3.7+**: Linguagem de programação usada para desenvolver a API.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
.
├── app
│   ├── main.py          # Arquivo principal da aplicação FastAPI.
│   ├── models.py        # Modelos Pydantic para validação de dados.
│   └── reservations.py  # Lógica para manipulação das reservas.
├── tabela
│   └── reservations.csv # Arquivo CSV para armazenar as reservas.
├── tests
│   └── test_api.py      # Testes para validar os endpoints da API.
└── README.md            # Documentação do projeto.
```

## Endpoints

A API possui os seguintes endpoints:

- `POST /reservations/`: Cria uma nova reserva. Os dados da reserva devem ser enviados como JSON no corpo da requisição.
- `GET /reservations/`: Lista todas as reservas existentes.

## Como Rodar Localmente

Para rodar a API localmente, siga estes passos:

1. Clone o repositório para sua máquina local.
2. Crie um ambiente virtual Python e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Acesse `http://127.0.0.1:8000/docs` no seu navegador para ver a documentação interativa da API.

## Executando Testes

Para executar os testes, certifique-se de que a API não está rodando e execute o seguinte comando no diretório raiz do projeto:

```bash
pytest tests/
```

## Contribuindo

Contribuições para a API são bem-vindas! Se você tem uma sugestão de melhoria, sinta-se à vontade para criar uma issue ou enviar um pull request.

---

Esperamos que este README forneça todas as informações necessárias para entender, rodar e testar a Hotel Reservation API. Se tiver dúvidas ou sugestões, por favor, abra uma issue no repositório.