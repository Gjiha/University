const express = require("express");
const morgan = require("morgan");
const app = express();

app.use(morgan("conbined"));

const cors = require("cors");
app.use(cors()); //autorizza il server a vedere anche le atre porte

const myMiddleware = function (req, res, next) {
	console.log("test middleware");
	next();
};

app.use(myMiddleware);
app.use(express.static("public")); //va a cercare le richieste all'interno di public

app.get("/data", (req, res) => {
	res.send("<h1> Ciao a tutti</h1>");
});

const checkAuth = function (req, res, next) {
	const authHeader = req.headers["authorization"];

	if (authHeader === "Bearer passwordsegreta") {
		next();
	} else {
		res.status(401).send("Non autorizzato");
	}
};

const sendData = function (req, res, next) {
	res.json({ message: "tutto okay" });
};

app.get("/secure", [checkAuth, sendData]);

const PORT = 9090;
app.listen(PORT, (err) => {
	if (err) {
		console.error(err.message);
	} else {
		console.log(`server in ascolto sulla porta ${PORT}`);
	}
});
