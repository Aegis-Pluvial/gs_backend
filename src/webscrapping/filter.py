from gs_backend.settings import Settings
from openai import OpenAI

AI_api_key = Settings().AI_api_key

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_api_key,)

prompt = (
    "Você receberá uma lista de 10 artigos sobre enchentes, contendo título e descrição. "
    "Seu trabalho é verificar se há alguma informação nova e recente sobre: "
    "1) dinheiro público perdido/gasto ou "
    "2) mortes. "
    "Ignore artigos que falem de eventos antigos, como '30 anos atrás...'. "
    "Só considere novidades recentes. "
    "Se encontrar algo novo, retorne uma lista com dois dicionários assim: "
    "[{'dinheiro_publico': 'valor'}, {'pessoas_mortas': 'quantidade'}] "
    "Se não houver nada novo, retorne apenas False."
    ""
    ""
    f"artigos:"
)

completion = client.chat.completions.create(model="openai/gpt-3.5-turbo",
                                             messages=[{"role": "user", "content": prompt}])


print(completion.choices[0].message.content)
