from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from gs_backend.settings import Settings

# Cria a engine base usada em todo o projeto. Chama o Objeto Settings para configurar o path da Database/
engine = create_engine(Settings().DATABASE_URL)


# Gerenciador de Contexto para abrir e fechar a Session automaticamente.
def get_session():  # Cria a sessão da conexão Sqlalchemy
    with Session(engine) as session:
        yield session
