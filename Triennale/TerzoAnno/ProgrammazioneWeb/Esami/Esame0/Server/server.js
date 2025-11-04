const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();

app.use(cors());

const data = JSON.parse(fs.readFileSync("data.json"));

app.get("/api/v1/data", (req, res) => {
	res.status(200).send({
		message: "ok",
		data: data,
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log(`Porta in ascolto sulla porta ${PORT}`);
});
