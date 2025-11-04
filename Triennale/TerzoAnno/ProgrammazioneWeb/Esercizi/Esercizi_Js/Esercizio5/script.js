"use strict";

let lista = ["ciao", "ciao2", "fraserandom", "ESQUIEEE"];

function addTitle(list) {
	let add = document.getElementById("addItem");

	let item = add.querySelector("h2");
	if (item != null) {
		add.removeChild(item);
	}
	item = document.createElement("h2");
	item.textContent = list[Math.floor(Math.random() * 4)];

	add.appendChild(item);
}

let btn = document.getElementById("btn");
btn.addEventListener("click", () => addTitle(lista));

let blue = document.getElementById("blue");
blue.addEventListener("click", () => {
	let div = document.getElementById("color");
	div.style.backgroundColor = "blue";
});

let reset = document.getElementById("reset");
reset.addEventListener("click", () => {
	let div = document.getElementById("color");
	div.style.backgroundColor = "aqua";
});

let form = document.getElementById("contactForm");
let message = document.getElementById("message");

form.addEventListener("submit", function (event) {
	event.preventDefault();
	let nome = document.getElementById("nome").value;
	let eMail = document.getElementById("email").value;

	if (nome === "" || eMail === "") {
		message.textContent = "Campi non riempiti correttamente";
	}
	message.textContent = `Benvenuto ${nome}, presto ti contatteremo presso l'e-mail ${eMail}`;
});
