"use strict";
const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let colors = JSON.parse(fs.readFileSync("data.json"));

let contatore = 5;

app.get("/counter", (req, res) => {
	res.status(200).json({
		message: "ok",
		data: { counter: contatore },
	});
});

app.post("/increase", (req, res) => {
	res.set("Content-type", "application/json");
	contatore += 1;
	res.status(200).json({
		message: "ok",
		data: { counter: contatore },
	});
});

app.post("/decrease", (req, res) => {
	res.set("Content-type", "application/json");
	contatore -= 1;
	res.status(200).json({
		message: "ok",
		data: { counter: contatore },
	});
});

app.get("/colors", (req, res) => {
	res.status(200).json({
		message: "ok",
		data: colors,
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log(`server in ascolto sulla porta ${PORT}`);
});
