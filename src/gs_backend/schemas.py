from pydantic import BaseModel


# Schemas do pydantic. Se é utilizado Typehint para facilitar a leitura
class Message(BaseModel):
    message: str


class StatusChange(BaseModel):
    change_status: int


class Article(BaseModel):
    title: str
    url: str
    published_at: str
    description: str


class ArticlesList(BaseModel):
    article: list[Article]


class NewData(BaseModel):
    deaths: int
    public_money: float
