from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa


#  >>>>>>>>>>>>>> VAMOS DEFINIR A ESTRUTURA BASE ANTES DE MONTAR <<<<<<<<<<<<

class Base(DeclarativeBase):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())


class ArticleDB(Base):
    __tablename__ = 'article'
    title = sa.Column(sa.String, nullable=False, unique=True)
    published_at = sa.Column(sa.String, nullable=False, unique=True)
    description = sa.Column(sa.String, nullable=False, unique=True)
    url = sa.Column(sa.String, nullable=False, unique=True)
