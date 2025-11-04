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
		data: data,
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
