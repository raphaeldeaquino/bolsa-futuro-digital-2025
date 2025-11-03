import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Novo post de teste",
    "body": "Conteúdo do post criado via API REST",
    "userId": 99
}

# Faz uma requisição POST com um corpo JSON
response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Retorno:")
print(response.json())
