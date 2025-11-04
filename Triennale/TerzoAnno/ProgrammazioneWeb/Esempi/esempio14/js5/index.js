const express = require("express");
const app = express();

app.get("/", (req, res) => {
	res.send("ciao");
});

app.get("/ciao", (req, res) => {
	res.send("ciao 2");
});

const PORT = 8080;
app.listen(PORT, (err) => {
	console.log(`Server in ascolto silla porta ${PORT}`);
});
