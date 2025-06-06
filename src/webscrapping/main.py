from gs_backend.settings import Settings
from urllib.request import urlopen
from urllib.parse import quote
from json import loads
from webscrapping.utils import add_article
from gs_backend.database import get_session
from webscrapping.utils import get_articles
session = next(get_session())

api_key = Settings().api_key
data = get_articles(session)
breakpoint()

query = quote(
    ('"enchente" AND ("mortes" OR "vítimas" OR "pessoas afetadas" OR "desabrigados" OR "danos" OR "prejuízo" OR '
     '"dinheiro público OR R$ OR dinheiro")'))

url = (f"https://gnews.io/api/v4/search?q={query}&lang=pt-BR&country=br&min=10&sortby=publishedAt&"
       f"&apikey={api_key}")

with urlopen(url) as response:
    data = loads(response.read().decode("utf-8"))
    articles = data["articles"]
    for i in range(len(articles)):
        add_article(article=articles[i], session=session)
        print(f"{i + 1}) Title: {articles[i]['title']}")
        print(f"{i + 1}) Description: {articles[i]['description']}")
        print(f"{i + 1}) Content: {articles[i]['content']}")
        print()
        print(f"{i + 1}) Publish Date: {articles[i]['publishedAt']}")
        print('================================================')
