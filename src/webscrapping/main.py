from gs_backend.settings import Settings
import urllib.request
import json

api_key = Settings.api_key
query = "enchente"  # Pode usar multiplas palavras, exemplos: Apple iPhone
url = f"https://gnews.io/api/v4/search?q={query}&lang=pt-BR&country=br&max=10&apikey={api_key}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]

    for i in range(len(articles)):
        # articles[i].title
        print(f"Title: {articles[i]['title']}")
        # articles[i].description
        print(f"Description: {articles[i]['description']}")
        break
        # You can replace {property} below with any of the article properties returned by the API.
        # articles[i].{property}
        # print(f"{articles[i]['{property}']}")
        # Delete this line to display all the articles returned by the request. Currently only the first article is displayed.
