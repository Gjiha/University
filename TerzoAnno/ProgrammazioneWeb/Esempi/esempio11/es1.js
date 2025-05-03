"use strict";

const promiseDelay = new Promise(function (resolve, reject) {
	setTimeout(function () {
		//resolve("hai vinto!");
		reject(new Error("Hai perso"));
	}, 5000);
});

promiseDelay.then((result) => console.log(result)).catch(console.error);
