"use strict";

function getColor() {
	return fetch("http://127.0.0.1:3000/colors")
		.then((res) => {
			if (!res.ok) throw new Error("errore riscontarto durante la fetch");
			return res.json();
		})
		.then((json) => {
			return json.data;
		})
		.catch((err) => {
			console.error(err);
		});
}

function getCounter(endPoint) {
	return fetch(endPoint)
		.then((res) => {
			if (!res.ok) throw new Error("fetch non anadata abuon fine");
			return res.json();
		})
		.then((json) => {
			return json.data.counter;
		})
		.catch((err) => {
			console.error(err);
		});
}

function postCounter(endPoint) {
	return fetch(endPoint, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
	})
		.then((res) => {
			if (!res.ok) throw new Error("fetch non anadata abuon fine");
			return res.json();
		})
		.then((json) => {
			return json.data.counter;
		})
		.catch((err) => {
			console.error(err);
		});
}

function setCounter(int) {
	let counter = document.getElementById("contatore");
	counter.textContent = int;
}

async function main() {
	let counter = await getCounter("http://127.0.0.1:3000/counter");
	setCounter(counter);

	let increaseBtn = document.getElementById("increase");
	increaseBtn.addEventListener("click", async () => {
		let counter = await postCounter("http://127.0.0.1:3000/increase");
		setCounter(counter);
	});

	let decreaseBtn = document.getElementById("decrease");
	decreaseBtn.addEventListener("click", async () => {
		let counter = await postCounter("http://127.0.0.1:3000/decrease");
		setCounter(counter);
	});

	let colorBtn = document.getElementById("color");
	colorBtn.addEventListener("click", async () => {
		let data = await getColor();
		let newColors = document.querySelectorAll(".newColor");

		newColors.forEach((el) => {
			el.style.backgroundColor = data.background;
			el.style.color = data.text;
		});
	});

	let hamburger = document.querySelector(".hamburger");
	let menu = document.getElementById("menu");
	hamburger.addEventListener("click", () => {
		hamburger.style.display = "none";
		menu.style.display = "flex";
	});
}

main();
