//si installano tramite npmm install
const moment = require("moment");
const dotenv = require("dotenv");
const chalk = require("chalk");

const bl = require("betterlog");

bl("ciao con un LOG");

const now = moment();

dotenv.config();
console.log(process.env.APIKEY);

console.log(now.format("HH:mm:ss"));

console.log(chalk.red("ciao a tutti!!"));
