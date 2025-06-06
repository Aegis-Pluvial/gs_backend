import os
from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from webscrapping.utils import change_statusDB
from gs_backend.schemas import Message, ArticlesList, StatusChange
from gs_backend.database import get_session
from gs_backend.models import ArticleDB, AlarmDB
from sqlalchemy import select
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()  # Monta o objeto base da API

# Configuração de pathing dos StaticFiles
current_dir = os.path.dirname(__file__)
static_dir = os.path.join(current_dir, "../static_files")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")  # Monta os arquivos estaticos

# ========================= HTML ROUTES ======================
templates = Jinja2Templates(directory=os.path.abspath(static_dir))


@app.get('/home/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

@app.get('/home/quiz', response_class=HTMLResponse)
def quiz(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("pages/quiz.html", context)

# ========================= API ROUTES ======================

# Path da API seguido pelo status code que irá retornar se a requisição for concluida e seguido pelo response model
# definido no pydantic
@app.get('/api/', status_code=200, response_model=Message)
def read_api_root():
    return {'message': 'api root'}  # Retorna mensagem para requisição feita


# Path de leitura dos articles cadastrados na DB hoje. Possui um "?q_limit" parametro de definição
# de quantos resultados será enviado pela API, e um response model de ArticlesList,
# ou seja, uma Lista contendo json de Articles
@app.get('/api/articles', response_model=ArticlesList, status_code=200)
# query_limit: int = 10 Cria um query
# parameter personalizavel que tem como padrão 10 resultados
def read_articles(q_limit: int = 10, session=Depends(get_session)):
    article = session.scalars(select(ArticleDB).limit(limit=q_limit))
    return {'article': article}


@app.get('/api/status', response_model=Message, status_code=200)
def read_status(session=Depends(get_session)):
    status = session.scalar(select(AlarmDB.status))
    status = str(status)
    return {'message': status}


@app.put('/api/status', response_model=Message, status_code=200)
def post_status(status: StatusChange, session=Depends(get_session)):
    change_statusDB(status=status, session=session)
    return {'message': 'Status Changed!'}
