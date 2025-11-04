const fs = require("fs");

const data = fs.readFileSync("data.json", "utf8"); //inizialmente data è solo una stringa di testo, l'estensione .json serve solo come nomenclatura

const data_json = JSON.parse(data); //in questo mommento il file .json da stringa diventa un oggetto javascript

// data_json.forEach((element) => {
// 	console.log(element);
// });

const data2 = JSON.parse(fs.readFileSync("data2.json", "utf8"));
console.log(data2["nome"]);

// console.log(data_json);
