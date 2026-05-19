# Decoratore
def saluto(funzione):

    # Funzione interna
    def wrapper():

        print("Prima della funzione")

        # Esegue la funzione originale
        funzione()

        print("Dopo la funzione")

    return wrapper


# Applico il decoratore
@saluto
def messaggio():
    print("Ciao Mirko!")


# Chiamata funzione
messaggio()

@saluto
def altraFunzione():
    print("hola Mirko")
    
    
#--------------------------------------------------------

# Variabile che simula il login

utente_loggato = True


# Decoratore
def richiede_login(funzione):

    def wrapper():

        if utente_loggato == True:
            funzione()
        else:
            print("Accesso negato")

    return wrapper


# Funzione protetta
@richiede_login
def area_personale():
    print("Benvenuto nell'area personale")


# Avvio
area_personale()

#--------------------------------------------------------


# Decoratore
def controllo(funzione):

    # *args raccoglie tutti i parametri posizionali
    def wrapper(*args):

        print("Avvio funzione")

        # Passa tutti i parametri alla funzione originale
        funzione(*args)

        print("Fine funzione")

    return wrapper


# Funzione decorata
@controllo
def somma(a, b, c):

    risultato = a + b + c

    print("Risultato:", risultato)
    
@controllo
def somma2(a, b, c, d):

    risultato = a + b + c + d

    print("Risultato:", risultato)


# Chiamata funzione
somma(5, 10, 15)

somma2(5, 10, 15, 20)


# --------------------------------------------------------------------------


# Decoratore
def log(funzione):

    # **kwargs raccoglie parametri con nome
    def wrapper(**kwargs):

        print("Dati ricevuti:")
        print(kwargs)

        # Passa i parametri alla funzione originale
        funzione(**kwargs)

    return wrapper


# Funzione decorata
@log
def utente(nome, età):

    print("Nome:", nome)
    print("Età:", età)
    return 1


# Chiamata funzione
utente(nome="Mirko", età=30)

#------------------------------------------------------------

# Primo decoratore
def decoratore1(funzione):

    def wrapper():

        print("Prima esecuzione")

        funzione()

        print("Fine primo decoratore")

    return wrapper


# Secondo decoratore
def decoratore2(funzione):

    def wrapper():

        print("Seconda esecuzione")

        funzione()

        print("Fine secondo decoratore")

    return wrapper


# Funzione decorata con due decoratori
@decoratore1
@decoratore2
def messaggio():

    print("Funzione originale")


# Avvio funzione
messaggio()