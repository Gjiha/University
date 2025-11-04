"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/persone", (req, res) => {
	console.log("richiesta GET/data ricevuta");
	res.status(200).json({
		message: "ok",
		data: data,
	});
});

app.get("/api/v1/persone/:id", (req, res) => {
	let id = parseInt(req.params.id);
	let newData;
	data.forEach((el) => {
		if (id === el.id) {
			newData = el;
		}
	});
	console.log("richiesta data ricevuta");
	res.status(200).json({
		message: "ok",
		data: newData,
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
