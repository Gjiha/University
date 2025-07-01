"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/items", (req, res) => {
	console.log("richiesta items ricevuta");
	res.status(200).json({
		message: "ok",
		data: data,
	});
});

app.get("/api/v1/items-complete", (req, res) => {
	console.log("richiesta items-complete ricevuta");
	let newData = [];
	data.forEach((el) => {
		if (el.completato === true) {
			newData.push(el);
		}
	});
	res.status(200).json({
		message: "ok",
		data: newData,
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
