from webscrapping.utils import get_articles
from gs_backend.database import get_session

session = next(get_session())
print(get_articles(session))
