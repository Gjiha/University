"use strict";

function getData() {
	return fetch("http://127.0.0.1:3000/data")
		.then((res) => {
			if (!res.ok) throw new Error("fetch non avvenuta correttamente");
			return res.json();
		})
		.then((json) => {
			return json.data;
		})
		.catch((err) => {
			console.error(err);
		});
}

function fill(message) {
	let container = document.getElementById("container");
	container.innerHTML = "";

	let jsonFile = document.createElement("pre");
	jsonFile.textContent = JSON.stringify(message, null, 2);
	jsonFile.className = "jsonFile";

	container.appendChild(jsonFile);
}

function convert(message) {
	let container = document.getElementById("container");
	container.innerHTML = "";
	let newUl = document.createElement("ul");

	message.forEach((el) => {
		let newLi = document.createElement("li");
		newLi.textContent = el.prodotto + " " + el.desc;
		newUl.appendChild(newLi);
	});

	container.appendChild(newUl);
}

async function main() {
	let message = await getData();
	fill(message);

	let converter = document.getElementById("converter");
	converter.addEventListener("click", () => {
		convert(message);
	});
}

main();
