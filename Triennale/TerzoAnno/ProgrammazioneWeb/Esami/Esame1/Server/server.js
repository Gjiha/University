"use strict";

const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(cors());

let data = JSON.parse(fs.readFileSync(path.join(__dirname, "data.json")));

app.get("/api/v1/data", (req, res) => {
	res.status(200).json({
		message: "ok",
		data: data,
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log(`sever in ascolto sulla porta ${PORT}`);
});
