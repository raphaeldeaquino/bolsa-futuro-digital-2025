const frases = [
  "Você é incrível!",
  "Hoje é um bom dia para sorrir!",
  "Confie no seu código!",
  "Seja a lenda do seu próprio script!",
];

const button = document.querySelector("button");

button.addEventListener("click", () => {
  const index = Math.floor(Math.random() * frases.length);
  document.body.style.backgroundColor = "#ffefd5";
  alert(frases[index]);
});
