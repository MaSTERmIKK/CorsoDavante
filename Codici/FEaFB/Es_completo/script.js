/*
  script.js
  SCOPO DIDATTICO:
  - Variabili (let/const)
  - Selezione elementi DOM (getElementById)
  - Eventi (addEventListener)
  - Funzioni
  - Condizioni (if/else)
  - Aggiornare testo in pagina (textContent)
  - Creare elementi (document.createElement)
  - Cicli (for)
*/

// ========== 0) PREPARAZIONE: "agganciare" gli elementi HTML ==========

// Prendiamo gli elementi dall'HTML tramite ID
const nomeInput = document.getElementById("nomeInput");
const btnSaluta = document.getElementById("btnSaluta");
const messaggio = document.getElementById("messaggio");

const btnMeno = document.getElementById("btnMeno");
const btnPiu = document.getElementById("btnPiu");
const contatoreSpan = document.getElementById("contatore");
const statoContatore = document.getElementById("statoContatore");

const itemInput = document.getElementById("itemInput");
const btnAggiungi = document.getElementById("btnAggiungi");
const btnSvuota = document.getElementById("btnSvuota");
const lista = document.getElementById("lista");

// ========== 1) SALUTO: input + bottone ==========

// Funzione che saluta leggendo il valore dell'input
function saluta() {
  // .value è il testo scritto dall'utente
  const nome = nomeInput.value;

  // Condizione: se è vuoto, chiediamo di scrivere qualcosa
  if (nome.trim() === "") {
    messaggio.textContent = "Scrivi un nome prima di salutare 🙂";
    return; // interrompe la funzione qui
  }

  // Altrimenti, scriviamo un messaggio personalizzato
  messaggio.textContent = "Ciao " + nome + "! Benvenuto/a 😊";
}

// Quando clicco il bottone, eseguo saluta()
btnSaluta.addEventListener("click", saluta);

// EXTRA: se premo Invio mentre sono sull'input, saluto
nomeInput.addEventListener("keydown", function (evento) {
  if (evento.key === "Enter") {
    saluta();
  }
});

// ========== 2) CONTATORE: +1 / -1 con logica ==========

// Variabile del contatore (parte da 0)
let contatore = 0;

// Aggiorna la parte grafica (DOM) in base al valore attuale
function aggiornaContatore() {
  contatoreSpan.textContent = contatore;

  // Un po' di logica per spiegare if/else
  if (contatore > 0) {
    statoContatore.textContent = "Il contatore è positivo.";
  } else if (contatore < 0) {
    statoContatore.textContent = "Il contatore è negativo.";
  } else {
    statoContatore.textContent = "Il contatore è neutro.";
  }
}

// Click su -1
btnMeno.addEventListener("click", function () {
  contatore = contatore - 1;
  aggiornaContatore();
});

// Click su +1
btnPiu.addEventListener("click", function () {
  contatore = contatore + 1;
  aggiornaContatore();
});

// ========== 3) LISTA DINAMICA: aggiungi e svuota ==========

// Aggiunge un elemento alla lista
function aggiungiElemento() {
  const testo = itemInput.value.trim();

  if (testo === "") {
    alert("Scrivi qualcosa prima di aggiungere!");
    return;
  }

  // Creiamo un <li> nuovo
  const li = document.createElement("li");
  li.textContent = testo;

  // Aggiungiamo il <li> dentro la <ul>
  lista.appendChild(li);

  // Svuotiamo l'input per comodità
  itemInput.value = "";
  itemInput.focus();
}

// Evento click
btnAggiungi.addEventListener("click", aggiungiElemento);

// Svuota la lista
btnSvuota.addEventListener("click", function () {
  // Metodo semplice: svuotare l'HTML interno
  lista.innerHTML = "";
});

// ========== 4) ESEMPIO CICLO: inserire 3 elementi iniziali ==========

// Una lista di partenza (array)
const esempiIniziali = ["HTML: struttura", "CSS: stile", "JS: logica"];

// Ciclo for: aggiunge automaticamente 3 elementi all'avvio
for (let i = 0; i < esempiIniziali.length; i++) {
  const li = document.createElement("li");
  li.textContent = esempiIniziali[i];
  lista.appendChild(li);
}
