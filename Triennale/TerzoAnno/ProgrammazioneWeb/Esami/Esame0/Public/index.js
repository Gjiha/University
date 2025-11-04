"use strict";

function fetchData(endPoint) {
	return fetch(endPoint)
		.then((res) => {
			if (!res.ok) throw new Error("http error");
			return res.json();
		})
		.then((json) => {
			return json.data;
		})
		.catch((err) => {
			console.error(err);
		});
}

function setArticles(array) {
	let wrapper = document.getElementById("wrapper");
	wrapper.innerHTML = "";
	array.forEach((art) => {
		let section = document.createElement("section");
		let title = document.createElement("h3");
		let arg = document.createElement("p");

		section.className = "section";

		title.textContent = art.titolo;
		arg.textContent = art.contenuto;

		wrapper.appendChild(section);
		section.appendChild(title);
		section.appendChild(arg);
	});
}

function shuffle(array) {
	array.sort(() => Math.random() - 0.5);
	return array;
}

function toggleMenu() {
	let menu = document.getElementById("menu");
	if (menu.style.display === "none") {
		menu.style.display = "flex";
	} else {
		menu.style.display = "none";
	}
}

function articleSwap(list) {
	setArticles(list);
}

async function main() {
	let list = await fetchData("http://127.0.0.1:3000/api/v1/data");
	setArticles(list);

	let btnMenu = document.getElementById("btnMenu");
	btnMenu.addEventListener("click", () => {
		if (window.innerWidth < 1000) {
			toggleMenu();
			if (btnMenu.style.color === "red") {
				btnMenu.style.color = "black";
			} else {
				btnMenu.style.color = "red";
			}
		}
	});

	let btnArticle = document.getElementById("btnArticle");
	btnArticle.addEventListener("click", () => {
		let newList = shuffle(list);
		articleSwap(newList);
	});
}

main();
