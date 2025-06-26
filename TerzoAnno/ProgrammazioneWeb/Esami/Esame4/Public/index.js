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

let global;
function loopLog(json) {
	json.forEach((el) => {
		console.log(el);
	});
}

function addDiv() {
	let container = document.getElementById("container");
	container.innerHTML = "";
	global.forEach((el) => {
		let div = document.createElement("div");
		div.style.height = "10vh";
		div.style.width = "10vh";
		div.style.position = "absolute";
		div.style.top = el.pos_vert + "%";
		div.style.left = el.pos_orizz + "%";
		div.style.backgroundColor = el.colore;
		div.addEventListener("click", () => {
			div.remove();
		});
		container.appendChild(div);
	});
}

async function main() {
	let fetch = await getData("http://127.0.0.1:3000/api/v1/data");
	global = fetch;
	loopLog(global);

	let title = document.getElementById("title");
	title.addEventListener("click", () => {
		addDiv();
	});
}

main();
