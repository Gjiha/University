"use strict";

function sum(a, b) {
	return a + b;
}

function diff(a, b) {
	return a - b;
}

function mul(a, b) {
	return a * b;
}

function calc() {
	let n1 = prompt("inserisci il primo numero");
	let n2 = prompt("inserisci il secondo numero");

	n1 = Number(n1);
	n2 = Number(n2);
	return sum(n1, n2);
}

function eseguiOperazione(a, b, operazione) {
	return operazione(a, b);
}

// alert(`il risultato della somma è ${calc()}`);

console.log(eseguiOperazione(3, 4, sum));
console.log(
	eseguiOperazione(3, 3, (a, b) => {
		return a / b;
	})
);
