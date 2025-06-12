# GS Backend

Backend para O Site Aegis-Pluvial. 

Atualização em Tempo Real Gerenciamento de artigos, webscraping e API RESTful.
## Estrutura do Projeto

---

```
gs_backend/
│
├── .env                      # Variáveis de ambiente (chaves, URLs, configs)
├── README.md                 # Este arquivo
│
├── src/
│   ├── gs_backend/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI app principal
│   │   ├── database.py       # Configuração do SQLAlchemy
│   │   ├── models.py         # Modelos ORM
│   │   ├── schemas.py        # Schemas Pydantic
│   │   ├── settings.py       # Configurações (env, chaves, etc)
│   │   └── ...               # Outros módulos internos
│   │
│   └── webscrapping/
│       ├── __init__.py
│       ├── utils.py          # Funções utilitárias para scraping
│       ├── main.py  # Script para automação diária de scraping
│       └── ...               # Outros scripts de scraping
│
└── tests/                    # Testes automatizados
```

## Principais Funcionalidades

- **API RESTful** com FastAPI para gerenciamento de artigos.
- **Banco de dados** via SQLAlchemy (SQLite/MySQL/Postgree, configurável via `.env`).
- **Webscraping** automatizado com scripts em `src/webscrapping/`.
- **Agendamento** de tarefas de scraping (exemplo: 100 requisições diárias).
- **Configuração centralizada** via arquivo `.env`.

## Como rodar o projeto

1. **Clone o repositório**
    ```sh
    git clone https://github.com/seu-usuario/gs_backend.git
    cd gs_backend
    ```

2. **Configure o ambiente**
    - Crie e edite o arquivo `.env` na raiz do projeto:
      ```
      api_key=SEU_API_KEY
      AI_api_key=SUA_AI_KEY
      DATABASE_URL=sqlite:///C:/Users/seu_usuario/PycharmProjects/gs_backend/database.db
      ```

3. **Instale as dependências**
    ```sh
    poetry install
    # ou
    pip install -r requirements.txt
    ```

4. **Rode a API**
    ```sh
    uvicorn src.gs_backend.main:app
    ```

5. **Execute o scraping diário**
    ```sh
    python src/webscrapping/main.py
    ```

## Comandos `taskipy`

Você pode usar os seguintes comandos no `pyproject.toml` com `taskipy`:

```toml
[tool.taskipy.tasks]
run = 'fastapi dev src/gs_backend/main.py --port 8000'
uvicorn = 'uvicorn gs_backend.main:app --port 8000'
run_lan = 'fastapi dev src/gs_backend/main.py --host 0.0.0.0'
test = 'pytest --cov=src/gs_backend -vv'
post_test = 'coverage html'
devpush = 'git push -u origin dev'
mainpush = 'git push -u origin main'
scrap = 'python src/webscrapping/main.py'
see_db = 'mycli -u root -p -h localhost -D articlesdb'
````

## Testes

Execute os testes com:
```sh
pytest
```

## Observações

- O caminho do banco de dados no `.env` deve ser absoluto para evitar múltiplos arquivos.
- Scripts de scraping podem ser agendados via cron (Linux) ou Task Scheduler (Windows).
- Ajuste as URLs e chaves conforme seu ambiente.
---

## Licença

MIT

---
