"use strict";

// let a = {"nome": "pippo"};
// let b = a;
// a == b //true

// let x = {};
// let y = {};
// x == y; //false

// funzioni legate ad oggetti

// let a = { name: "pippo" };
// a.saluta = function () {
// 	alert("ciao pippo");
// };
// a.saluta();

// a.name = "pluto";
// a.saluta = function () {
// 	alert("Ciao " + this.name); //faccio in modo di avere una funzione che varia il proprio comportamento in base ai campi dell'oggetto
// };

// costruttore

// function User(name) {
// 	this.name = name;
// 	this.isAdmin = false;
// 	// implicitamente ritorna this
// }

// let user = new User("Pippo"); // se ometto il new sto attacando le proprietà alla finestra del browser
// alert(user.name);
// alert(user.isAdmin);

//funzioni builtIn

// function printhello() {
// 	console.log("Ciao");
// }

// let i = setInterval(printhello(), 5000);

// //funzioni innestate

// function counter() {
// 	let a = 0;
// 	return {
// 		inc: function () {
// 			++a;
// 		},
// 		dec: function () {
// 			--a;
// 		},
// 		get: function () {
// 			return a;
// 		},
// 		reset: function () {
// 			a = 0;
// 		},
// 	};
// }

// let c = counter();
// c.inc();

// prototipi

function Course(course_name) {
	this.name = course_name;
}

let pw = new Course("programmazione web");
let p = new Course("programmazione");

Course.prototype.university = "Tor Vergata";
Course.prototype.address = "Via del politecnico"; //prototype è solo delle funzioni

console.log(p.address);
console.log(p.__proto__); //proto è solo degli oggetti
