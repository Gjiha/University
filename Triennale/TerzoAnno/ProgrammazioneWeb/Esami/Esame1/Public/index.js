"use strict";

function getData(endPoint) {
	return fetch(endPoint)
		.then((res) => {
			return res.json();
		})
		.then((json) => {
			return json.data;
		})
		.catch((err) => {
			console.error(err);
		});
}

function fill(list) {
	let wrapper = document.getElementById("wrapper");
	wrapper.innerHTML = "";
	list.forEach((arg) => {
		let div = document.createElement("div");
		let h3 = document.createElement("h3");

		h3.textContent = arg.titolo;

		div.className = "container";
		h3.className = "title";

		div.style.backgroundColor = arg.colore;

		div.appendChild(h3);
		wrapper.appendChild(div);
	});
}

function btnClose() {
	let over = document.getElementById("over");
	if (over.style.display === "none") {
		over.style.display = "flex";
	} else {
		over.style.display = "none";
	}
}

async function main() {
	let list = await getData("http://127.0.0.1:3000/api/v1/data");
	let btn = document.getElementById("btn");

	btn.addEventListener("click", () => btnClose());

	fill(list);
}

main();
