let nome = "Mario";
let eta = 25;

// Salvataggio dei dati
localStorage.setItem("nomeUtente", nome);
localStorage.setItem("etaUtente", eta);

// Recupero dei dati salvati
let nomeSalvato = localStorage.getItem("nomeUtente");
let etaSalvata = localStorage.getItem("etaUtente");

// Visualizzazione dei risultati
console.log("Nome:", nomeSalvato);
console.log("Età:", etaSalvata);

// Eliminazione di un dato
localStorage.removeItem("etaUtente");