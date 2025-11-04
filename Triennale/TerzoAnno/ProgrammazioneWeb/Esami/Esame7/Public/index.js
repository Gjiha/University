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
	let i = index;
	let gallery = document.getElementById("gallery");
	let ul = document.createElement("ul");
	while (index < i + 4 && index < data.length) {
		let li = document.createElement("li");
		let a = document.createElement("a");
		a.innerText = data[index];
		a.className = "link";
		li.appendChild(a);
		ul.appendChild(li);
		index += 1;
		a.addEventListener("click", function () {
			getInformation(parseInt(a.innerText));
		});
	}
	if (ul.querySelectorAll("li").length != 0) {
		gallery.appendChild(ul);
	}
}

async function getInformation(id) {
	let data = await getData(`http://127.0.0.1:3000/api/v1/pics/${id}`);
	let banner = document.getElementById("banner");
	banner.style.display = "flex";
	let p = document.getElementById("indication");
	p.innerText = data.desc;
	p.style.color = "white";
	p.style.fontSize = "30px";
}

let index = 0;

async function main() {
	let data = await getData("http://127.0.0.1:3000/api/v1/list");
	fillMain(data);
	let button = document.querySelector("button");
	button.addEventListener("click", () => {
		fillMain(data);
	});
}

main();
