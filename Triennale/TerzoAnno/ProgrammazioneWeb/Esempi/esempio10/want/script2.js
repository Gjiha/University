"use strict";

let freddySentences = ["ride my bycicle", "break free", "it all", "it now"];

function changeImage() {
	let random;
}

document.getElementById("submit").addEventListener("click", function () {
	let randomSentece =
		freddySentences[Math.floor(Math.random() * freddySentences.length())];
	console.log(randomSentece);
	//add the sentece to the list
	let list = document.getElementById("want-list");
	let txt = document.createElement("li");
});
