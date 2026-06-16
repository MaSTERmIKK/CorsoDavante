

def funzioni ():
    pass


#definizione di funzione
def es_par (a,b):  # tra le psratesi si chiamano parametri
    return a + b

#richiamo della funzione
x = es_par("mirko", " ciao")
print(es_par(2,3), x)

def es_tipi (x:str):
    print("ciao come " + x)
      
es_tipi("stai")
    
def es_default( z = "predef"):
    print(z)

es_default()
es_default("pippo")

def controllori(x):
    c = True
    if x == "si":
        c = False
    else:
        c = True
    return c


controllo = controllori("no")

while(controllo):
    
    print("operazioni")
    
    scelta = input("vuoi smettere di ripetere? scrivi si per uscire").lower()
    
    controllo = controllori(scelta)
    


def somma(a):
    return a+a

def potenza(a):
    return a*a


def calcolo_ops(a,b):
    
    print(a + b)

calcolo_ops(somma(10), potenza(20))


def es_ricorsiva(a):
    
    if a < 100:
        print(a)
        a +=1
        es_ricorsiva(a)
    else:
        print(es_ricorsiva.__name__)
        print("finito")
        
es_ricorsiva(80)


def stampa(x):
    print(x, stampa.__name__)
    
def doppia_chiamata(lista):
    somma = 0
    for i in lista:
        somma +=i
    
    stampa(somma)
    return somma

lista = [1,2,3]
doppia_chiamata(lista)
    
    
    
    