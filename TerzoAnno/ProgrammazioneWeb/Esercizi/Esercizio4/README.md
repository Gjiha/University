# Esercizi CSS

Si realizzi il file style.css nel quale vanno scritte delle regole per il file index.html in accordo alle 10 specifiche seguenti. 

Per ogni regola css si dichiari in un commento nel file la specificità del selettore. Un esempio di regola css con calcolo della specificità è il seguente:
```
/*Spec (0,0,0,1)*/
p {
	color: black;
}
```
## **Parte 1: Stili Generali (Ereditati)**

Questi stili saranno applicati agli elementi principali della pagina, ma potrebbero essere sovrascritti da regole più specifiche.

1. **Stile generale del corpo della pagina**

   - Imposta il colore del testo di tutto il documento a **nero** e il font a **Arial**.

2. **Stile del testo nelle sezioni principali**

   - Imposta il colore del testo nei `<header>`, `<main>`, `<footer>` a **blu scuro** e la dimensione del font a **16px**.

3. **Stile dei link generali**

   - Imposta il colore di tutti i link `<a>` su **verde** e cambia in **rosso** quando il mouse passa sopra.

4. **Stile generale dei titoli**

   - Imposta il colore di tutti gli `<h1>`, `<h2>`, `<h3>` su **arancione** e rendili in **grassetto**.

5. **Stile delle liste**

   - Cambia il colore del testo di tutti i `<li>` contenuti in un `<ul>` a **marrone** e aggiungi un margine di **10px**.

---

## **Parte 2: Stili Specifici (Collisioni con Ereditati)**

Questi stili hanno una specificità maggiore e possono sovrascrivere gli stili generali.

6. **Stile specifico per il menu di navigazione**

   - Cambia il colore dei link all'interno del menu `.menu` in **bianco** con sfondo **blu scuro**.

7. **Stile dei titoli specifici**

   - Cambia il colore del titolo `<h1>` principale in **rosso**.

8. **Stile personalizzato per i paragrafi evidenziati**

   - Imposta il colore del testo dei paragrafi con classe `.evidenziato` a **giallo**.

9. **Stile delle liste dettagliate**

   - Cambia il colore dei `<li>` dentro `.lista` a **viola**, sovrascrivendo il colore marrone ereditato.

10. **Stile del footer personalizzato**

   - Imposta il colore del testo del `<footer>` in **grigio chiaro**, sovrascrivendo il blu scuro ereditato.

---

### **Esercizio Extra**

- Modifica il colore di tutti i link nel menu `.menu a` in **giallo**, ma assicurati che quelli nel `.submenu` rimangano **bianchi**.
