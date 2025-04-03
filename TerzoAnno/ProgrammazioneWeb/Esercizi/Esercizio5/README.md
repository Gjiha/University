# 🧱 Esercizio CSS: Box Model & Background


## 📄 HTML di partenza (da scrivere)

Struttura HTML nel `<body>`:

```html
<div class="box-esercizio">
  Questo è un contenitore da stilizzare con il CSS.
</div>

<div class="box-secondo">
  Secondo box con sfondo diverso e testo centrato.
</div>
```

---

## 🔧 Parte 1 – Box Model

1. Imposta al `.box-esercizio`:
   - `width: 300px;`
   - `height: 150px;`
   - `padding: 20px;`
   - `border: 2px solid blue;`
   - `margin: 30px auto;` *(il box sarà centrato orizzontalmente)*
   - `box-sizing: border-box;`

2. Cambia `box-sizing` in `content-box` e verifica come cambia la dimensione visiva.

---

## 🎨 Parte 2 – Background

### Step 1 – Colore

- Imposta `background-color: #f0f0f0;` al `.box-esercizio`.
- Cambia il colore del testo in `#333`.
- Aggiungi un’ombra (`box-shadow`).

### Step 2 – Immagine da Picsum

- Aggiungi l'immagine come sfondo:
  ```css
  background-image: url('https://picsum.photos/300/150');
  ```
- Imposta:
  - `background-repeat: repeat;`  
    *(lascia il valore di default e osserva l’effetto)*
- Poi, modifica:
  - `background-repeat: no-repeat;`
  - `background-position: center;`
  - `background-size: cover;`

> ✏️ *Prova anche `contain` al posto di `cover` e nota le differenze.*

---

## 🧪 Parte 3 – Secondo box e confronto

Per `.box-secondo`:

- Imposta `width` e `height` uguali al primo.
- Cambia `border` in `3px double green`.
- Imposta:
  ```css
  background-image: url('https://picsum.photos/seed/pattern/300/150');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  ```
- Centra il contenuto **verticalmente e orizzontalmente** con Flexbox.

---

## 📏 Osservazione sul collasso dei margini

Aggiungi questa regola a entrambi i box:
```css
margin-bottom: 30px;
```

E poi rimuovila **dal secondo** box per vedere il comportamento:

> ❓ *Quanto margine resta visibile tra i due box? Perché non è 60px?*

📚 **Spiegazione attesa**:
Quando due elementi block consecutivi hanno margini verticali, questi possono “**collassare**” e non si sommano. Il margine finale sarà pari al maggiore dei due, non alla loro somma.
