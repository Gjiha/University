"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync("data.json"));

app.get("/data", (req, res) => {
	res.status(200).json({
		message: "ok",
		data: data,
	});
});

app.use((req, res) => {
	res.status(400).json({
		message: "api not implemented",
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
