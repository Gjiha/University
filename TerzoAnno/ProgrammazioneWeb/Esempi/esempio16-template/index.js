const express = require('express')
const app = express()
const path = require("path")

//aggancio il sistea di view dinamica
app.set("view engine", "ejs")
app.set("views",path.join(__dirname,'views'))

app.get("/",(req, res) => {
    res.render("home",{messaggio: "che bella giornata di sole oggi, posso andare a giocare a tennis"})
})

app.get("/prodotti",(req, res) => {

    const listaProdotti = ["latte", "uova", "vino", "farina"]
    res.render("prodotti",{listaProdotti : listaProdotti, messaggio : "Oggi sconti per tutti!"})
})


app.listen(9999,(err) => {
    console.log("Running")
})