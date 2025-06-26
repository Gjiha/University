"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/articoli", (req, res) => {
	console.log("richiesta articoli ricevuta");
	res.status(200).json({
		message: "ok",
		data: data,
	});
});

app.get("/api/v1/autori", (req, res) => {
	console.log("richiesta autori ricevuta");
	let list = [];
	data.forEach((el) => {
		list.push(el.autore);
	});
	res.status(200).send({
		message: "ok",
		data: list,
	});
});

app.post("/increase", (req, res) => {
	res.set("Content-type", "application/json");
	res.status(200).json({
		message: "ok",
		data: "", //aggiungere dati!!!!!!!!
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
