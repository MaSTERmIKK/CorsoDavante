#ESERCIZIO (TESTO)
#Crea un programma che gestisca un oggetto Libro.
#Ogni libro deve avere: titolo, autore e numero di pagine.
#Il programma deve:
#Creare almeno due libri
#Stampare le informazioni dei libri
#Verificare quale libro ha più pagine



# Definizione della classe Libro
class Libro:
    def __init__(self, titolo, autore, pagine):
        # Attributi dell'oggetto
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # Metodo per stampare le informazioni del libro
    def stampa_info(self):
        print("Titolo:", self.titolo)
        print("Autore:", self.autore)
        print("Pagine:", self.pagine)
        print("---------------------")


# Creazione di due oggetti Libro
libro1 = Libro("Il Signore degli Anelli", "Tolkien", 1200)
libro2 = Libro("1984", "Orwell", 328)

# Stampa delle informazioni
libro1.stampa_info()
libro2.stampa_info()

# Confronto tra i libri
if libro1.pagine > libro2.pagine:
    print("Il libro con più pagine è:", libro1.titolo)
else:
    print("Il libro con più pagine è:", libro2.titolo)
