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
	let main = document.querySelector("main");
	main.innerHTML = "";
	data.forEach((el) => {
		let box = document.createElement("div");
		box.className = "box";
		let p = document.createElement("p");
		p.innerText = el.testo;
		let button = document.createElement("button");
		if (el.completato) {
			button.innerText = "Completato";
			p.style.textDecoration = "line-through";
			button.style.border = "none";
			button.style.color = "#a1a1a1";
		} else {
			button.innerText = "Completa";
		}
		box.appendChild(p);
		box.appendChild(button);
		main.appendChild(box);
	});
}

async function main() {
	let allData = await getData("http://127.0.0.1:3000/api/v1/items");
	fillMain(allData);
	let completati = document.getElementById("soloCompletati");
	completati.addEventListener("click", async () => {
		let completedData = await getData(
			"http://127.0.0.1:3000/api/v1/items-complete"
		);
		fillMain(completedData);
	});
	let mostraTutti = document.getElementById("mostraTutti");
	mostraTutti.addEventListener("click", async () => {
		let allData = await getData("http://127.0.0.1:3000/api/v1/items");
		fillMain(allData);
	});
	let body = document.querySelector("body");
	let scuro = document.getElementById("scuro");
	scuro.addEventListener("click", () => {
		body.className = "darkTheme";
	});
	let chiaro = document.getElementById("chiaro");
	chiaro.addEventListener("click", () => {
		body.className = "whiteTheme";
	});
}

main();
