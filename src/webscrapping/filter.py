from gs_backend.settings import Settings
from openai import OpenAI
from webscrapping.utils import get_articles, add_status
from gs_backend.database import get_session
import ast

AI_api_key = Settings().AI_api_key
session = next(get_session())

# Configuração do Client openrouter.ai
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=AI_api_key, )

# Variavel que recebe uma lista com os objetos do sqlalchemy.
# Objetos contém os titulos e as descrições dos artigos coletados
articles = get_articles(session)

# ListComprehensions que desempacota os objetos do sqlalchemy e concatena em uma string legivel á IA.
complete_articles = "\n".join([f"\nTítulo: {article.title}\n "
                               f"Descrição: {article.description}" for article in articles])

prompt = (
    "Você receberá uma lista de artigos sobre enchentes, contendo título e descrição. "
    "Seu trabalho é verificar se há alguma informação nova e recente sobre: "
    "1) dinheiro público perdido/gasto ou "
    "2) mortes. "
    "Ignore artigos que falem de eventos antigos, como '30 anos atrás...'. "
    "Só considere novidades recentes. "
    "Se encontrar algo novo, retorne uma lista com dois dicionários assim: "
    "[{'dinheiro_publico': 'valor'}, {'pessoas_mortas': 'quantidade'}], substituindo 'valor' pelo valor encontrado "
    "e 'quantidade' pela quantidade de mortes novas. "
    "Se não houver nenhuma informação nova, retorne exatamente: "
    "[{'dinheiro_publico': 'None'}, {'pessoas_mortas': 'None'}].\n\n"
    "Responda SOMENTE no formato pedido. NÃO gere texto explicativo.\n\n"
    f"{complete_articles}"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",  # Modelo da IA
    messages=[
        {"role": "user", "content": prompt}
    ],
    # Variaveis de configuração da IA para uma leitura mais precisa.
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

# Try Except que filtra se os dados que a IA enviou foram corretos ou não.
try:
    data = response.choices[0].message.content  # Desempacota a primeira mensagem enviada pela IA
    data = ast.literal_eval(data)  # Converte a resposta para uma lista de dicionarios.
    add_status(session=session, status=data)  # Adiciona os dados na tabela status
except TypeError:
    data = None
except KeyError:
    data = None

