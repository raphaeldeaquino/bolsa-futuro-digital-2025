import requests

def buscar_status():
    resp = requests.get("https://api.exemplo/status")
    # BUG: retorna chave errada "stat" em vez de "status"
    return resp.json().get("stat")