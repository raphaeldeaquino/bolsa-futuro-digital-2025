async function enviarNome() {
  const nome = document.getElementById("nome").value;

  const resposta = await fetch("/api/elogio", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ nome: nome })
  });

  const dados = await resposta.json();
  document.getElementById("resposta").innerText = dados.mensagem;
}
