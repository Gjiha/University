"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/data", (req, res) => {
	console.log("richiesta GET/data ricevuta");
	res.status(200).json({
		message: "ok",
		data: "", //aggiungere dati!!!!!!!!
	});
});

app.post("/api/v1/post", (req, res) => {
	res.set("Content-type", "application/json"); //ATTENZIONE AL PARAMETRO
	res.status(200).json({
		message: "ok",
		data: "", //aggiungere dati!!!!!!!!
	});
});

app.get("/api/v1/data/:id", (req, res) => {
	console.log("richiesta id ricevuta");
	let id = parseInt(req.params.id);
	let newEl;
	let find = false;
	data.forEach((el) => {
		if (id === el.id) {
			//template id !!MODIFICA OPPORTUNAMENTE
			find = true;
			newEl = el;
		}
	});
	if (find) {
		res.status(200).json({
			message: "ok",
			data: "", //aggiungere dati!!!!!!!!
		});
	} else {
		res.status(404).json({
			message: "not ok",
			error: "id non pervenuto",
		});
	}
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
