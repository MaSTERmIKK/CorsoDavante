#Attento alle lezioni gaetano.

import random

# 1. Numero casuale da 0 a 100 e visualizzarlo
numero_casuale = random.randint(0, 100)
print("Numero casuale:", numero_casuale)

# 2. Chiedere il nome all'utente e mostrarlo
nome = input("Inserisci il tuo nome: ")
print("Ciao,", nome)

# 3. Numero casuale e confronto con numero inserito dall'utente
numero_casuale = random.randint(0, 100)
numero_utente = int(input("Indovina il numero (0-100): "))
if numero_utente == numero_casuale:
    print("Bravo! Hai indovinato!")
else:
    print(f"Sbagliato. Il numero era {numero_casuale}")

# 4. Creare una lista di numeri e mostrarla
numeri = [10, 20, 30, 40, 50]
print("Lista di numeri:", numeri)

# 5. Lista di stringhe ordinata per lunghezza
parole = ["mela", "banana", "kiwi", "arancia"]
parole_ordinate = sorted(parole, key=len)
print("Lista ordinata per lunghezza:", parole_ordinate)

# 6. Creare una tupla di stringhe e visualizzarla
tupla_stringhe = ("ciao", "mondo", "python")
print("Tupla di stringhe:", tupla_stringhe)

# 7. Creare una tupla con elementi di tipo diverso
tupla_mista = (42, "testo", 3.14, True)
print("Tupla con elementi diversi:", tupla_mista)

# 8. Aggiungere un elemento alla tupla (convertendola in lista e viceversa)
tupla_mista = (42, "testo", 3.14, True)
lista_mista = list(tupla_mista)  # Convertire in lista
lista_mista.append("nuovo elemento")  # Aggiungere
tupla_mista = tuple(lista_mista)  # Riconvertire in tupla
print("Tupla aggiornata:", tupla_mista)

# 9. Convertire una tupla in stringa
tupla_caratteri = ('P', 'y', 't', 'h', 'o', 'n')
stringa = "".join(tupla_caratteri)
print("Tupla come stringa:", stringa)

# 10. Contare le occorrenze di un numero in una tupla
tupla_numeri = (1, 2, 3, 2, 4, 2, 5)
numero_da_contare = 2
conteggio = tupla_numeri.count(numero_da_contare)
print(f"Il numero {numero_da_contare} appare {conteggio} volte nella tupla.")

# 11. Verificare se una lettera è nella tupla di lettere
tupla_lettere = ('a', 'b', 'c', 'd', 'e')
lettera = input("Inserisci una lettera: ")
if lettera in tupla_lettere:
    print(f"La lettera '{lettera}' è presente nella tupla.")
else:
    print(f"La lettera '{lettera}' non è presente nella tupla.")
