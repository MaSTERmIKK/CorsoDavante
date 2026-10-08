nome_lista = [ 22,44,00,11 ]  #questo è mutabile
nome_tupla = ( "esempio",11,22,"MIRKO" )  #questo è immutabile
print(nome_lista)
print(nome_lista[0])

#questo è la modifica per indice
nome_lista[1] = "modifica"
print(nome_lista)

#questo è l'inserimento al fondo
nome_lista.append(55)
print(nome_lista)

#questo è la rimozione per valore
nome_lista.remove("modifica")
print(nome_lista)

#questo è l'inserimento per posizione
nome_lista.insert(2,33)
print(nome_lista)

#questo è l'ordinamento
nome_lista.sort()
print(nome_lista)

#questo è l'ordinamento
nome_lista.clear()
print(nome_lista)

#Unpaking della tupla
a,b,c,d = nome_tupla
print(a,b,c,d)

#insiemi
nome_insieme2 = {22,44,00,11 }  
nome_insieme1 = {22,34,00,21 } 

#inserimento e rimozione
nome_insieme1.add(21)
nome_insieme1.remove(21)

#differenza tra insiemi
print(nome_insieme1.difference(nome_insieme2))
print(nome_insieme2.difference(nome_insieme1))

#interssezione tra insiemi
print(nome_insieme1.intersection(nome_insieme2))


# Creazione di un dizionario
studente = {
    "nome": "Mario",
    "eta": 21,
    "corso": "Informatica"
}

#stampa dei dizionari
print(studente["eta"])

#modifica chiave dizionario
studente["eta"] = 24
print(studente)

#creazione nuova chiave dizionario
studente["media"] = 9
print(studente)

#inserimento di collezioni in collezioni
studente["voti"] = nome_lista
print(studente)
