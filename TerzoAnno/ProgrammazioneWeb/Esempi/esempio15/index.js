const express = require("express");
const app = express();
const PORT = 8080;

app.listen(PORT, (err) => {
	console.log(`server in ascolto sulla porta ${PORT}`);
});

app.get("/", (req, res) => {
	res.send("Home");
});

app.get("/about", (req, res) => {
	res.send("About");
});

app.post("/about", (req, res) => {
	res.set("Content-type", "text/plain");
	res.send("About POST");
});

app.get("/contact", (req, res) => {
	res.set("Content-type", "text/plain");
	res.send("Contact");
	console.log();
});

app.post("/contact", (req, res) => {
	res.status(201).send("Contatti Post");
});

app.get("/users/:id/aula/:aula", (req, res) => {
	console.log(req.params);
	res.send("USER");
});

const routerUsers = express.Router();

// POST /users/login
routerUsers.post("/login", (req, res) => {
	console.log(req.params);
	res.send("POST Login");
});

// GET /users/logout
routerUsers.get("/logout", (req, res) => {
	res.send("GET Logout");
});

app.use("/users", routerUsers);
