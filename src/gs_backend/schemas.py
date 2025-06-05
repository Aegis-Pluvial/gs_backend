from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Article(BaseModel):
    title: str
    url: str
    published_at: str
    description: str


class ArticlesList(BaseModel):
    article: list[Article]

