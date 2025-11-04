const express = require("express");
const app = express();
const bodyparser = require("body-parser");

app.use(express.static("public"));
app.use(bodyparser.urlencoded());

app.get("/elabData", (req, res) => {
	const data = req.query;

	let { corso, nome } = res.query;

	console.log(data);
	res.send(`<h1>Dati ricevuti ${nome}</h1>`);
});

app.post("/elabData", (req, res) => {
	const data = req.body;
	console.log(data);
	res.send(`<h1> POST dati ricevuti</h1>`);
});

app.listen(8080, () => {
	console.log("Server in ascolto sulla porta 8080");
});
