"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/citations", (req, res) => {
	console.log("richiesta citation ricevuta");
	res.status(200).json({
		message: "ok",
		data: data,
	});
});

app.get("/api/v1/citations/:id", (req, res) => {
	console.log("richiesta id ricevuta");
	let id = parseInt(req.params.id);
	let newEl;
	let find = false;
	data.forEach((el) => {
		if (id === el.ID) {
			find = true;
			newEl = el;
		}
	});
	if (find) {
		res.status(200).json({
			message: "ok",
			data: newEl,
		});
	} else {
		res.status(404).json({
			message: "not ok",
			error: "id non pervenuto",
		});
	}
});

app.use((req, res) => {
	res.status(400).json({
		message: "not ok",
		error: "url inesistente",
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
