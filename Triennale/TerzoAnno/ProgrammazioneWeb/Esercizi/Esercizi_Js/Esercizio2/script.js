"use strict";

function callBack() {
	let a = 0;
	return {
		inc: () => {
			a += 1;
			return a;
		},
		dec: () => {
			a -= 1;
			return a;
		},
		mul: (b) => {
			a *= b;
			return a;
		},
	};
}

let cont = callBack();

console.log(cont.inc());
console.log(cont.inc());
console.log(cont.dec());
console.log(cont.mul(3));

function messageBroker(string) {
	return function message() {
		console.log(`questo è un prefisso: ${string}`);
	};
}

messageBroker("ciao")();

function compose(f, g, x) {
	return f(g(x));
}

console.log(
	compose(
		(x) => 3 + x,
		(x) => 3 - x,
		4
	)
);

function provaTempo(int, operation) {
	return setInterval(operation, int);
}

console.log(provaTempo(2000, () => console.log("ciao")));
