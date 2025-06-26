"use strict";

function getData(endPoint) {
	return fetch(endPoint)
		.then((res) => {
			if (!res.ok) throw new Error("errore riscontrato durante la fetch");
			return res.json();
		})
		.then((json) => {
			return json.data;
		})
		.catch((err) => {
			console.log(err);
		});
}

function fillMain(data) {
	let person = document.getElementById("persone");
	person.innerHTML = "";
	let ul = document.createElement("ul");
	data.forEach((el) => {
		let li = document.createElement("li");
		li.innerText = el.nome + " " + el.cognome;
		ul.appendChild(li);
		li.addEventListener("click", function () {
			alert("nome: " + el.nome + el.cognome + "età: " + el.età);
		});
	});
	person.appendChild(ul);
}

function aggiornaColori() {
	let body = document.querySelector("body");
	let links = document.querySelectorAll("a");
	body.style.backgroundColor = "#00796b";
	links.forEach((el) => {
		el.style.color = "#313131";
	});
}

async function main() {
	let data = await getData("http://127.0.0.1:3000/api/v1/persone");
	fillMain(data);
	let button = document.getElementById("aggiornaColori");
	button.addEventListener("click", () => {
		aggiornaColori();
	});
}

main();
