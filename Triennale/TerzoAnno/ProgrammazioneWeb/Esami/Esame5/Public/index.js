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
	let container = document.getElementById("articleContainer");
	container.innerHTML = "";
	data.forEach((el) => {
		let box = document.createElement("div");
		box.className = "box";
		let title = document.createElement("h3");
		title.innerText = el.titolo;
		let aut = document.createElement("p");
		aut.innerHTML = "<strong>Autore</strong>: " + el.autore;
		let desc = document.createElement("p");
		desc.innerText = el.contenuto;
		let newButton = document.createElement("button");
		newButton.innerText = "Mostra dettagli";
		newButton.addEventListener("click", function () {
			alert(
				"titolo: " +
					el.titolo +
					"\nautore: " +
					el.autore +
					"\ndescrizione: Lorem Ipsum...."
			);
		});
		box.appendChild(title);
		box.appendChild(aut);
		box.appendChild(desc);
		box.appendChild(newButton);
		container.appendChild(box);
	});
}

function fillModal(author) {
	let modal = document.getElementById("section");
	modal.innerHTML = "";
	let ul = document.createElement("ul");
	author.forEach((el) => {
		let li = document.createElement("li");
		li.innerText = el;
		ul.appendChild(li);
	});
	modal.appendChild(ul);
}

async function main() {
	let data = await getData("http://127.0.0.1:3000/api/v1/articoli");
	let author = await getData("http://127.0.0.1:3000/api/v1/autori");
	fillMain(data);
	fillModal(author);
	let final = document.getElementById("finalButton");
	final.addEventListener("click", () => {
		let modal = document.getElementById("modal");
		modal.style.display = "block";
		let overlay = document.getElementById("overlay");
		overlay.style.display = "block";
	});
	let close = document.getElementById("close");
	close.addEventListener("click", () => {
		let modal = document.getElementById("modal");
		modal.style.display = "none";
		let overlay = document.getElementById("overlay");
		overlay.style.display = "none";
	});

	let hamburger = document.querySelector(".hamburger");
	hamburger.addEventListener("click", () => {
		let hamburger = document.querySelector(".hamburger");
		hamburger.style.display = "none";
		let menu = document.querySelector(".menu");
		menu.style.display = "flex";
	});
}

main();
