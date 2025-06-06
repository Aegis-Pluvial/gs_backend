from gs_backend.models import ArticleDB, StatusDB, AlarmDB
from sqlalchemy import select
from sqlalchemy.orm import Session
from gs_backend.schemas import StatusChange


def get_articles(session: Session):
    data = session.scalars(select(ArticleDB)).all()
    return data


def check_article(title: str, session: Session):
    data = session.scalars(select(ArticleDB).where(ArticleDB.title == title))
    return data.all()


def add_article(article, session: Session):
    article_db = ArticleDB(title=article["title"], url=article["url"], published_at=article["publishedAt"],
                           description=article["description"])
    session.add(article_db)
    session.commit()
    session.refresh(article_db)


def add_status(session: Session, status: list):
    deaths = status[1]['pessoas_mortas']
    money = status[0]['dinheiro_publico']
    status_db = session.scalar(select(StatusDB).where(StatusDB.id == 1))
    status_db.deaths = deaths
    status_db.money = money
    session.commit()
    session.refresh(status_db)


def change_statusDB(session: Session, status: StatusChange):
    status_db = session.scalar(select(AlarmDB).where(AlarmDB.id == 1))
    status_db.status = status.change_status
    session.commit()
    session.refresh(status_db)

def get_status_death(session: Session):
    data = session.scalar(select(StatusDB.deaths))
    data = str(data)
    return data

def get_status_money(session: Session):
    data = session.scalar(select(StatusDB.money))
    data = str(data)
    return data


