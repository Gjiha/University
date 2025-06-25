"use strict";

function Persona(nome, cognome, eta) {
	this.nome = nome;
	this.cognome = cognome;
	this.eta = eta;
}

let persona1 = new Persona("francesco", "cosciotti", 22);

// console.log(persona1);
// console.log(persona1.eta);

persona1.cognome = "non più cosciotti";
persona1.occupazione = "nuova occupazione";
// console.log(persona1);

let x = Object.keys(persona1).length;
// console.log(x);

function Studente(nome, voto) {
	this.nome = nome;
	this.voto = voto;
}

let studente2 = new Studente("a4", 2);
let studente3 = new Studente("a6", 3);
let studente4 = new Studente("ap", 4);
let studente5 = new Studente("ai", 5);
let studente6 = new Studente("ay", 6);
let studente7 = new Studente("ad", 7);
let studente8 = new Studente("ac", 8);

let studenteArray = [
	studente2,
	studente3,
	studente4,
	studente5,
	studente6,
	studente7,
	studente8,
];

function countStudentGrade(arr) {
	let newArr = [];
	let treshold = 6;
	for (let student of arr) {
		if (student.voto >= treshold) {
			newArr.push(student);
		}
	}
	return newArr;
}

function sommaVoti(arr) {
	let sum = 0;
	for (let student of arr) {
		sum += student.voto;
	}
	return sum;
}

function bestStudent(arr) {
	let temp = 0;
	let bestStudent;
	for (let student of arr) {
		if (student.voto > temp) {
			bestStudent = student;
		}
	}
	return bestStudent;
}

function cloneObj(obj) {
	let copy = {};
	for (let key of Object.keys(obj)) {
		if (typeof obj === Object) {
			copy[key] = cloneObj(obj[key]);
		} else {
			copy[key] = obj[key];
		}
	}
	return copy;
}

persona1.innested = [1, 3];

let clone = cloneObj(persona1);
clone.innested = { 3: "no" };
console.log(persona1);
console.log(clone);

// console.log(countStudentGrade(studenteArray));
// console.log(sommaVoti(studenteArray));
// console.log(bestStudent(studenteArray));
