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

function postData(endPoint) {
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

async function main() {
	let data = await getData("");
}

main();
