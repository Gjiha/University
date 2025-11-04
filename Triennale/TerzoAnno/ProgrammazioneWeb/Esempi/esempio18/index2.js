const express = require("express");
const app = express();
const cors = require("cors");

app.use(express.json());
app.use(cors());

app.post("/data", (req, res) => {
	const data = req.body;
	console.log(data);
	res.json({
		status: "success",
		message: "Dati ricevuti con successo",
	});
});

const PORT = 3000;
app.listen(PORT, () => {
	console.log("server in ascolto sulla porta 3000");
});
