def fattoriale(n):
    # Base case: il fattoriale di 0 è 1
    if n == 0:
        return 1
    # Caso ricorsivo: n * fattoriale di (n-1)
    else:
        return n * fattoriale(n-1)

# Esempio di utilizzo della funzione
print(fattoriale(5))  # Output: 120

def is_palindromo(parola):
    # Convertire la parola in minuscolo per standardizzare la verifica
    parola = parola.lower()
    # Controllare se la parola è uguale alla sua versione rovesciata
    return parola == parola[::-1]

x = "Anna"
# Esempio di utilizzo della funzione
print(is_palindromo(x))  # Output: True


def mcd(a, b):
    # Continua a eseguire il loop finché b non diventa zero
    while b != 0:
        # Aggiorna a e b con b e il resto della divisione a / b
        a, b = b, a % b
    # Quando b è zero, a è l'MCD
    return a

y= 54

z = 24

# Esempio di utilizzo della funzione
print(mcd(y, z))  # Output: 6


def genera_primi(n):
    primi = []
    numero = 2  # Il primo numero primo
    while len(primi) < n:
        # Iterare attraverso tutti i numeri fino alla radice quadrata di "numero"
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                break
        else:
            # Se non si trovano divisori, aggiungere il numero alla lista dei primi
            primi.append(numero)
        numero += 1
    return primi

# Esempio di utilizzo della funzione
print(genera_primi(5))  # Output: [2, 3, 5, 7, 11]


def conta_vocali(testo):
    # Definire un set di vocali
    vocali = set("aeiouAEIOU")
    contatore = 0
    # Contare ogni carattere nel testo se è una vocale
    for carattere in testo:
        if carattere in vocali:
            contatore += 1
    return contatore

# Esempio di utilizzo della funzione
print(conta_vocali("Hello World"))  # Output: 3


def ricerca_lineare(lista, elemento):
    # Scorrere ogni elemento nella lista
    for indice, valore in enumerate(lista):
        # Se l'elemento è trovato, restituire l'indice
        if valore == elemento:
            return indice
    # Se l'elemento non è nella lista, restituire -1
    return -1

# Esempio di utilizzo della funzione
print(ricerca_lineare([1, 3, 5, 7, 9], 7))  # Output: 3


def unisci_dizionari(diz1, diz2):
    # Unire due dizionari usando l'operatore di unpacking
    return {**diz1, **diz2}

# Esempio di utilizzo della funzione
dizionario1 = {'a': 1, 'b': 2}
dizionario2 = {'b': 3, 'c': 4}


print(unisci_dizionari(dizionario1, dizionario2))  # Output: {'a': 1, 'b': 3, 'c': 4}



def inverti_stringa(s):
    # Restituire la stringa invertita
    return s[::-1]

# Esempio di utilizzo della funzione
print(inverti_stringa("python"))  # Output: "nohtyp"




def merge_sort(lista):
    # Se la lista contiene meno di due elementi, è già ordinata
    if len(lista) <= 1:
        return lista

    # Dividere la lista in due parti
    metà = len(lista) // 2
    sinistra = merge_sort(lista[:metà])
    destra = merge_sort(lista[metà:])

    # Unire le due liste ordinate
    def merge(sinistra, destra):
        ordinata = []
        i = j = 0

        # Ordinare gli elementi fino a quando non si esauriscono in una delle due liste
        while i < len(sinistra) and j < len(destra):
            if sinistra[i] < destra[j]:
                ordinata.append(sinistra[i])
                i += 1
            else:
                ordinata.append(destra[j])
                j += 1

        # Aggiungere gli elementi rimanenti dalle due liste
        ordinata.extend(sinistra[i:])
        ordinata.extend(destra[j:])
        return ordinata

    return merge(sinistra, destra)

# Esempio di utilizzo della funzione
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # Output: [3, 9, 10, 27, 38, 43, 82]



def cifra_cesare(testo, chiave):
    risultato = ""
    # Scorrere ogni carattere nel testo
    for carattere in testo:
        # Se il carattere è una lettera maiuscola
        if carattere.isupper():
            # Spostare il carattere in avanti di "chiave" posizioni, gestendo il wrap-around con modulo 26
            risultato += chr((ord(carattere) + chiave - 65) % 26 + 65)
        # Se il carattere è una lettera minuscola
        elif carattere.islower():
            risultato += chr((ord(carattere) + chiave - 97) % 26 + 97)
        # Se non è una lettera, lasciarlo invariato
        else:
            risultato += carattere
    return risultato

def decifra_cesare(testo, chiave):
    # Decifrare è come cifrare, ma spostando indietro
    return cifra_cesare(testo, -chiave)

# Esempio di utilizzo delle funzioni
testo_cifrato = cifra_cesare("Hello, World!", 3)
print(testo_cifrato)  # Output: "Khoor, Zruog!"
print(decifra_cesare(testo_cifrato, 3))  # Output: "Hello, World!"
