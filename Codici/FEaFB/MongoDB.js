// Importo MongoClient dalla libreria mongodb
const { MongoClient } = require("mongodb");

// Creo l'indirizzo del server MongoDB locale
const url = "mongodb://localhost:27017";

// Creo il client, cioè l'oggetto che gestisce la connessione
const client = new MongoClient(url);

// Funzione principale asincrona
async function main_connesione() {

    try {
        // Apro la connessione al server MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database chiamato scuola
        const db = client.db("scuola");

        // Seleziono la collezione chiamata studenti
        const studenti = db.collection("studenti");

        console.log("Database selezionato: scuola");
        console.log("Collezione selezionata: studenti");

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante la connessione:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}


// Funzione principale asincrona
async function main_inserimento() {

    try {
        // Apro la connessione a MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database scuola
        const db = client.db("scuola");

        // Seleziono la collezione studenti
        const studenti = db.collection("studenti");

        // Creo un documento JavaScript sotto forma di oggetto
        const nuovoStudente = {
            nome: "Luca",
            eta: 22,
            corso: "Python",
            voto: 28
        };

        // Inserisco il documento nella collezione
        const risultato = await studenti.insertOne(nuovoStudente);

        // Stampo l'id del documento inserito
        console.log("Documento inserito con ID:");
        console.log(risultato.insertedId);

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante l'inserimento:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}



// Funzione principale asincrona
async function main_inserimento() {

    try {
        // Apro la connessione a MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database scuola
        const db = client.db("scuola");

        // Seleziono la collezione studenti
        const studenti = db.collection("studenti");

        // Cerco il primo studente che ha nome Luca
        const studente = await studenti.findOne({
            nome: "Luca"
        });

        // Stampo il documento trovato
        console.log("Studente trovato:");
        console.log(studente);

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante la lettura:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}


// Funzione principale asincrona
async function main_filtro() {

    try {
        // Apro la connessione a MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database scuola
        const db = client.db("scuola");

        // Seleziono la collezione studenti
        const studenti = db.collection("studenti");

        // Cerco tutti gli studenti con voto maggiore o uguale a 28
        const risultati = await studenti.find({
            voto: { $gte: 28 }
        }).toArray();

        // Stampo gli studenti trovati
        console.log("Studenti con voto maggiore o uguale a 28:");

        for (let studente of risultati) {
            console.log(studente);
        }

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante la lettura:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}



// Funzione principale asincrona
async function main_aggiornamento() {

    try {
        // Apro la connessione a MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database scuola
        const db = client.db("scuola");

        // Seleziono la collezione studenti
        const studenti = db.collection("studenti");

        // Aggiorno il voto dello studente Luca
        const risultato = await studenti.updateOne(
            {
                nome: "Luca"
            },
            {
                $set: {
                    voto: 30
                }
            }
        );

        // Stampo quanti documenti sono stati modificati
        console.log("Documenti trovati:");
        console.log(risultato.matchedCount);

        console.log("Documenti modificati:");
        console.log(risultato.modifiedCount);

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante l'aggiornamento:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}


// Funzione principale asincrona
async function main_eliminazione() {

    try {
        // Apro la connessione a MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database scuola
        const db = client.db("scuola");

        // Seleziono la collezione studenti
        const studenti = db.collection("studenti");

        // Elimino il primo studente con nome Marco
        const risultato = await studenti.deleteOne({
            nome: "Marco"
        });

        // Stampo quanti documenti sono stati eliminati
        console.log("Documenti eliminati:");
        console.log(risultato.deletedCount);

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante l'eliminazione:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}


// Funzione principale asincrona
async function main_ordinamento() {

    try {
        // Apro la connessione a MongoDB
        await client.connect();

        console.log("Connessione a MongoDB riuscita");

        // Seleziono il database scuola
        const db = client.db("scuola");

        // Seleziono la collezione studenti
        const studenti = db.collection("studenti");

        // Ordino gli studenti per voto dal più alto al più basso
        const risultati = await studenti.find().sort({
            voto: -1
        }).toArray();

        // Stampo gli studenti ordinati
        console.log("Studenti ordinati per voto dal più alto al più basso:");

        for (let studente of risultati) {
            console.log(studente);
        }

    } catch (errore) {

        // Se qualcosa va male, stampo l'errore
        console.log("Errore durante l'ordinamento:");
        console.log(errore);

    } finally {

        // Chiudo la connessione
        await client.close();

        console.log("Connessione chiusa");
    }
}

// Avvio il programma



