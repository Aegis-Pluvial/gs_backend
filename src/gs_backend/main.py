import os
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from gs_backend.schemas import Message, ArticlesList
from gs_backend.database import get_session
from gs_backend.models import ArticleDB
from sqlalchemy import select

app = FastAPI()
current_dir = os.path.dirname(__file__)
static_dir = os.path.join(current_dir, "../static_files")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")


@app.get('/api/', status_code=200, response_model=Message)
def read_api_root():
    return {'message': 'api root'}


@app.get('/api/articles', response_model=ArticlesList, status_code=200)
# query_limit: int = 10 Cria um query
# parameter personalizavel que tem como padrão 10 resultados
def read_users(query_limit: int = 1, session=Depends(get_session)):
    article = session.scalars(select(ArticleDB).limit(limit=query_limit))
    return {'article': article}
