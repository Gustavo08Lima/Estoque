import requests

# A URL da sua API rodando localmente
url = "http://127.0.0.1:8000/itens/42"
parametros = {"q": "python_tutorial"}

# Fazendo a requisição GET
response = requests.get(url, params=parametros)

if response.status_code == 200:
    dados = response.json()
    print(f"Sucesso! O item retornado foi: {dados['item_id']}")
else:
    print(f"Erro: {response.status_code}")