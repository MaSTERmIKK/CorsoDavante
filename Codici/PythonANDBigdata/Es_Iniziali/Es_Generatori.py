# da fare tramite --> file = open( "prova.txt","r") con nome file reale e nella stessa cartella

def leggi_file(nome_file):
    """Generatore: legge il file riga per riga"""
    with open(nome_file) as f:
        for riga in f:
            yield riga

def filtra_errori(righe):
    """Generatore: filtra solo le righe con ERROR"""
    for r in righe:
        if "ERROR" in r:
            yield r

def estrai_messaggio(righe):
    """Generatore: estrae solo il messaggio utile"""
    for r in righe:
        yield r.split(" - ")[-1].strip()

def processa_log(file):
    """Pipeline completa"""
    return estrai_messaggio(
        filtra_errori(
            leggi_file(file)
        )
    )

# Uso
for messaggio in processa_log("log.txt"):
    print(messaggio)