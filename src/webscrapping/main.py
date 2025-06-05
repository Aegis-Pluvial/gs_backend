from gs_backend.settings import Settings
from urllib.request import urlopen
from urllib.parse import quote
from json import loads

api_key = Settings().api_key
query = quote(
    ('"enchente" AND ("mortes" OR "vítimas" OR "pessoas afetadas" OR "desabrigados" OR "danos" OR "prejuízo" OR '
     '"dinheiro público OR R$ OR dinheiro")'))

url = f"https://gnews.io/api/v4/search?q={query}&lang=pt-BR&country=br&min=10&sortby=publishedAt&apikey={api_key}"

with urlopen(url) as response:
    data = loads(response.read().decode("utf-8"))
    articles = data["articles"]

    for i in range(len(articles)):
        print(f"{i + 1}) Title: {articles[i]['title']}")
        print(f"{i + 1}) Description: {articles[i]['description']}")
        print(f"{i + 1}) Content: {articles[i]['content']}")
        print()
        print(f"{i + 1}) Publish Date: {articles[i]['publishedAt']}")
        print('================================================')
