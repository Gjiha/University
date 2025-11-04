"use strict";

//operatori

let a, b;

a = "5";
b = 5;
//alert(a == b); // true -> effetua in automatico la conversione
//alert(a === b); // false -> il classico ==

let x;

x = a && b; // AND
x = a || b; // OR
x = a ?? b; // operatore che torna a se definito, ovvero non è undefined, altrimenti b

// variabili truly e falsy

x = 0; // x è falsy ovvero tendente al falso, sono variabili di tipo 0, "", null, undefined
let y = 5; // il resto è truly

//I cicli sono identici a C

//dichiarazione di funzioni

function somma(a, b) {
	return a + b;
}

function calcolatrice() {
	let n1, n2, ret;

	n1 = prompt("inserisci il primo numero");
	n2 = prompt("inserisci il secondo numero"); // prompt crea una finestra che richiede un input
	n1 = Number(n1); // esegue il cancel
	n2 = Number(n2);

	ret = somma(n1, n2);
	alert("la somma è " + ret); // dà una finestra senza input
}

calcolatrice();

//prova di funzioni passate come parametri

function ask(question, yes, no) {
	if (confirm(question)) {
		yes();
	} else {
		no();
	}
}

ask(
	"ti chiami pippo ?",
	function () {
		alert("ciao pippo");
	},
	function () {
		alert("ciao anonimo");
	}
);
