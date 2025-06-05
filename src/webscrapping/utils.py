from gs_backend.models import ArticleDB
from sqlalchemy import select
from sqlalchemy.orm import Session


# def get_lastDate(session: Session):
#     data = session.scalars(select(ArticleDB).where(ArticleDB.published_at))
#     return data


# def get_articles(session: Session):
#     data = session.scalars(select(ArticleDB))
#     return data


def add_article(article, session: Session):
    article_db = ArticleDB(title=article["title"], url=article["url"], published_at=article["publishedAt"],
                           description=article["description"])
    session.add(article_db)
    session.commit()
    session.refresh(article_db)
