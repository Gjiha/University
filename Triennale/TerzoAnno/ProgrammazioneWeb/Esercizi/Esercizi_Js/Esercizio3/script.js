"use strict";

let a = [1, 2, 3, 4, 5, 6, 7];
console.log(a.map((x) => 2 * x));

console.log(a);

function Persona(name, surname, eta) {
	this.name = name;
	this.surname = surname;
	this.eta = eta;
	this.saluta = () => {
		console.log(`ciao sono ${name + " " + surname}`);
	};
}

let arr = [];

for (let i = 0; i < 10; i += 1) {
	arr.push(new Persona("a", "b", Math.floor(Math.random() * 10)));
}

let maxARR = arr.reduce((acc, utente) => {
	if (utente.eta > acc.eta) {
		return utente;
	}
	return acc;
}, arr[0]);

console.log(arr);
console.log(maxARR);
