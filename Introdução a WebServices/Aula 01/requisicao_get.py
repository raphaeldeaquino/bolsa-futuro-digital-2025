import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Faz uma requisição GET
response = requests.get(url)

# Exibe o código de status e parte da resposta
print("Status:", response.status_code)
print("Exemplo de retorno:")
print(response.json())
