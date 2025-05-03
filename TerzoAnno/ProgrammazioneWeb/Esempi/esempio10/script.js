"use script";
window.onload = function () {
	//da aggiungere altrimenti viene eseguito lo script prima che venga caritato l'html
	document.getElementById("myDiv").addEventListener("click", function () {
		alert("Bravo");
	});
};

function moveDiv() {
	let div = document.getElementById("myDiv");
	let rndX = Math.floor(Math.random() * (window.innerWidth - 300));
	let rndY = Math.floor(Math.random() * (window.innerHeight - 300));
	div.style.position = "absolute";
	div.style.left = rndX + "px";
	div.style.top = rndY + "px";
	if (div.style.color === "black") {
		div.style.backgroundColor = "white";
		body.style.backgroundColor = "black";
	} else {
		div.style.backgroundColor = "black";
		body.style.backgroundColor = "white";
	}
}

setInterval(moveDiv(), 5000);
