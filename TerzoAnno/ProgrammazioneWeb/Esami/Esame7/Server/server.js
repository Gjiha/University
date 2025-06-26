"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/list", (req, res) => {
	console.log("richiesta list ricevuta");
	let idList = [];
	data.forEach((el) => {
		idList.push(el.id);
	});
	res.status(200).json({
		message: "ok",
		data: idList,
	});
});

app.get("/api/v1/pics/:id", (req, res) => {
	console.log("richiesta pics ricevuta");
	let id = parseInt(req.params.id);
	let request;
	let find = false;
	data.forEach((el) => {
		if (el.id === id) {
			find = true;
			request = el;
			res.status(200).json({
				message: "ok",
				data: request,
			});
		}
	});
	if (!find) {
		res.status(404).json({
			message: "error",
			error: "id non pervenuto",
		});
	}
});

app.use((req, res) => {
	res.status(400).json({
		message: "not ok",
		error: "url errato",
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
