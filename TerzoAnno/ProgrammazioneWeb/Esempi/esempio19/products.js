const express = require("express");
const router = express.Router();
const fs = require("fs");

const wine_list = JSON.parse(fs.readFileSync("data/products.json"));

router.get("/", (req, res) => {
	res.json({
		status: "success",
		data: {},
	});
});

router.get("/:id", (req, res) => {
	const id = req.params.id;
	const wine = wine_list.find((el) => parseInt(el.id) === id);

	if (!wine) {
		return res.status(404).json({
			status: "fail",
			message: `ID ${id} non trovato`,
		});
	}

	res.json({
		status: "success",
		data: wine,
	});
});

router.post("/", (req, res) => {
	const data = req.body;
	console.log(data);

	if (!data.nome || !data.cantina) {
		return res.status(422).json({
			status: "error",
			message: "dati mancanti",
		});
	}

	const new_id = wine_list[wine_list.length - 1].id + 1;
	data.id = new_id;

	wine_list.push(data);

	res.json({
		status: "success",
		data: data,
	});
});

module.exports = router;
