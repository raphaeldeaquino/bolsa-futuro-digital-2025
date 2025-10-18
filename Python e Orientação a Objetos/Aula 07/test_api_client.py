from unittest.mock import patch
from api_client import buscar_status

def test_buscar_status_mock(monkeypatch):
    class Dummy:
        def json(self):
            return {"status": "ok"}  # resposta correta da API (esperada)

    def fake_get(url):
        return Dummy()

    monkeypatch.setattr("api_client.requests.get", fake_get)
    resultado = buscar_status()
    assert resultado == "ok"  # FALHA: buscar_status busca "stat" e retorna None