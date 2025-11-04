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

async function fillBox(ID) {
	let data = await getData(`http://127.0.0.1:3000/api/v1/citations/${ID}`);
	let box = document.getElementById("red");
	box.innerHTML = "";
	box.style.display = "flex";
	let p = document.createElement("p");
	let valore = document.createElement("p");
	p.innerText = data.frase;
	valore.innerText = data.valore;
	box.appendChild(p);
	box.append(valore);
}

function fillMain(data) {
	let container = document.getElementById("container");
	data.forEach((el) => {
		let li = document.createElement("li");
		li.innerText = el.ID;
		container.appendChild(li);
		li.addEventListener("click", function () {
			fillBox(parseInt(el.ID));
		});
	});
}

async function main() {
	let data = await getData("http://127.0.0.1:3000/api/v1/citations");
	fillMain(data);
}

main();
