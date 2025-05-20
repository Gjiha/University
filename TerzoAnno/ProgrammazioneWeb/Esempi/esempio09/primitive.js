let giorno = [
	"lunedì",
	"martedì",
	"mercoledì",
	"giovedì",
	"venerdì",
	"sabato",
	"domenica",
];

let i = 0;
while (i < giorno.length) {
	giorno.unshift(giorno.pop()); // unshift aggiunge in testa, pop elimina dalla fine, diminuisce la lunghezza e ritorna l'ultimo vslore
}

let names = ["mario", "giovanni", "pippo"];

names = names.map((item) => "Dr." + item.toUpperCase()); // la funzione map itera su tutti gli elementi dell'array ed esegue operazioni su esso
names.reduce(
	(acc, item, idx, arr) => (item.length() > arr[acc].length() ? idx : acc, 0)
);
// acc -> accumulatore,                  if item.lenght() > arr[acc].lenght(){acc = idx}else{acc=acc}
