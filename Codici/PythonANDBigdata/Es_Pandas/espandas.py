# Analisi delle Vendite di un Negozio: Hai un DataFrame vendite che contiene 
# le seguenti colonne: 'Data', 'Prodotto', 'Quantità', 'Prezzo_Unitario'. 
# Il tuo compito è:
# Calcolare il fatturato totale per ogni prodotto.
# Trovare il prodotto più venduto in termini di quantità.
# Creare un nuovo DataFrame che mostra il fatturato per ogni mese.


import pandas as pd

# Creiamo un DataFrame di esempio per le vendite
data = {'Data': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'Prodotto': ['Mela', 'Banana', 'Mela', 'Pera'],
        'Quantità': [30, 50, 40, 60],
        'Prezzo_Unitario': [0.50, 0.30, 0.50, 0.30]}

vendite = pd.DataFrame(data)

# Calcoliamo il fatturato totale per prodotto
vendite['Fatturato'] = vendite['Quantità'] * vendite['Prezzo_Unitario']
fatturato_prodotto = vendite.groupby('Prodotto')['Fatturato'].sum()
print("Fatturato totale per prodotto:\n", fatturato_prodotto)

# Troviamo il prodotto più venduto in termini di quantità
prodotto_piu_venduto = vendite.groupby('Prodotto')['Quantità'].sum().idxmax()
print("\nProdotto più venduto:", prodotto_piu_venduto)

# Creiamo un nuovo DataFrame per il fatturato mensile
vendite['Data'] = pd.to_datetime(vendite['Data'])
fatturato_mensile = vendite.groupby(vendite['Data'].dt.to_period('M'))['Fatturato'].sum()
print("\nFatturato mensile:\n", fatturato_mensile)


# Esplorazione Dati Meteo: 
# Supponi di avere un DataFrame meteo che registra quotidianamente la temperatura (in gradi Celsius), 
# l'umidità (%) e la velocità del vento (km/h) per diverse città. 
# Le colonne sono: 'Data', 'Città', 'Temperatura', 'Umidità', 'Velocità_Vento'. 
# Il tuo compito è:
# Calcolare la temperatura media, l'umidità media, e la velocità media del vento per ogni città.
# Identificare la città con la temperatura più alta registrata e la data in cui è avvenuto.
# Calcolare la variazione della temperatura media mensile per ogni città.

import pandas as pd

# Creiamo un DataFrame di esempio per i dati meteo
data = {'Data': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'Città': ['Roma', 'Milano', 'Roma', 'Milano'],
        'Temperatura': [20, 15, 21, 16],
        'Umidità': [70, 65, 75, 68],
        'Velocità_Vento': [10, 5, 15, 7]}
meteo = pd.DataFrame(data)





# Calcoliamo medie per ogni città
medie_città = meteo.groupby('Città').mean()
print("Medie per città:\n", medie_città)

# Troviamo la città con la temperatura più alta e la data
temp_max = meteo[meteo['Temperatura'] == meteo['Temperatura'].max()]
print("\nCittà con temperatura più alta:\n", temp_max[['Data', 'Città', 'Temperatura']])

# Calcoliamo la variazione della temperatura media mensile per città
meteo['Data'] = pd.to_datetime(meteo['Data'])
temp_media_mensile = meteo.groupby(['Città', meteo['Data'].dt.to_period('M')])['Temperatura'].mean()
print("\nVariazione della temperatura media mensile per città:\n", temp_media_mensile)


# Scenario: 
# Hai un DataFrame studenti che contiene informazioni sugli studenti
# e i loro voti in diverse materie.
# Le colonne sono: 'Nome', 'Matematica', 'Scienze', 'Letteratura', 'Storia', 'Arte'. 

data = {'Nome': ['Alice', 'Bruno', 'Chiara', 'Davide'],
        'Matematica': [8, 6, 7, 9],
        'Scienze': [7, 9, 6, 8],
        'Letteratura': [8, 6, 9, 7],
        'Storia': [6, 7, 8, 9],
        'Arte': [9, 8, 7, 6]}

# Il tuo compito è:
# Calcolare il voto medio per ogni studente.
# Trovare la materia con la media voto più alta.
# Identificare gli studenti con un voto medio superiore a 8.
