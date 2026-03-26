/*
ESERCIZIO (TESTO)
Crea un programma che gestisca un oggetto Libro.
Ogni libro deve avere: titolo, autore e numero di pagine.

Il programma deve:

Creare almeno due libri
Stampare le informazioni dei libri
Verificare quale libro ha più pagine

*/

// Definizione della classe Libro
class Libro {
    String titolo;
    String autore;
    int pagine;

    // Costruttore
    public Libro(String titolo, String autore, int pagine) {
        this.titolo = titolo;
        this.autore = autore;
        this.pagine = pagine;
    }

    // Metodo per stampare le informazioni
    public void stampaInfo() {
        System.out.println("Titolo: " + titolo);
        System.out.println("Autore: " + autore);
        System.out.println("Pagine: " + pagine);
        System.out.println("---------------------");
    }
}

// Classe principale
public class Main {
    public static void main(String[] args) {

        // Creazione degli oggetti
        Libro libro1 = new Libro("Il Signore degli Anelli", "Tolkien", 1200);
        Libro libro2 = new Libro("1984", "Orwell", 328);

        // Stampa informazioni
        libro1.stampaInfo();
        libro2.stampaInfo();

        // Confronto tra i libri
        if (libro1.pagine > libro2.pagine) {
            System.out.println("Il libro con più pagine è: " + libro1.titolo);
        } else {
            System.out.println("Il libro con più pagine è: " + libro2.titolo);
        }
    }
}
