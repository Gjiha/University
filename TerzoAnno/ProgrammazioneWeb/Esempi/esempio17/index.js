const express = require("express");
const fs = require("fs");
const app = express();

const data = JSON.parse(fs.readFileSync("prof.json"));

//3 punti d'esame
app.get("/api/v1/profs", (req, res) => {
	res.status(200).json(data);
});

//3 punti d'esame
app.get("/api/v1/profs/:id", (req, res) => {
	const id = parseInt(req.params.id);
	const prof = data.find((el) => {
		el.id === id;
		return data[id];
	});
	if (prof) {
		res.status(200).json(prof);
	} else {
		res.status(404).json({ message: "data not found" }); //bisogna ritornare qualcosa altrimenti non chiude la connessione
	}
});

app.listen(3000, (err) => {
	if (err) {
		console.log(err.message);
	} else {
		console.log("Server in ascolto sulla porta 3000");
	}
});
