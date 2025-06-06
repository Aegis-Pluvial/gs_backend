from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa


# Modelo de Tabela base. Contem ID e Created AT, como colunas base que irá ter em toda tabela
class Base(DeclarativeBase):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())  # Função fun.now() chama a func
    # datetime, que irá definir o horario exato que o dado ta tabela foi criado.


# Tabela de armazenamento de Artigos. Contem os dados dos artigos recolhidos pela Gnews API
class ArticleDB(Base):
    __tablename__ = 'article'
    title = sa.Column(sa.VARCHAR(500), nullable=False, unique=True)
    published_at = sa.Column(sa.VARCHAR(500), nullable=False, unique=True)
    description = sa.Column(sa.VARCHAR(500), nullable=False, unique=True)
    url = sa.Column(sa.VARCHAR(500), nullable=False, unique=True)


# Tabela de Status. Irá recolher do filter.py os status mais recentes.
class StatusDB(Base):
    __tablename__ = 'status'
    deaths = sa.Column(sa.VARCHAR(500), nullable=False, unique=True)
    money = sa.Column(sa.VARCHAR(500), nullable=False, unique=True)


class AlarmDB(Base):
    __tablename__ = 'alarm'
    status = sa.Column(sa.Integer, nullable=False, unique=True)
