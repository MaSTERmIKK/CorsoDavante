


# Questo si chiama while!
# e un commando che ci permette di creare un ciclo o un interatore

i = 0

while (i < 5):  # condizionalità di ripetizione // finchè la condizione ripèorta true si ripeterà 
 
 i += 1   # aumenta la nostra variabile d'iterazione
 if (i == 6): 
    continue                # break,  continue  else
 print(i)   # printa la nostra variabile d'iterazione
else:       
 print("il ciclo è finito")
 
i = 0 
x = 10

while (i <= 5 or x >= 8 ):  
 print(i, x)
 x -=1
 i +=1

i=0 
x=10
while (i <= 5 and x >= 8 ):  
 print(i, x)
 x -=1
 i +=1
 
i=0
x=10
while (i <= 5 or x >= 8 ):  
 while(x != 0 ):
  print(i, x)
  x -=1
  i +=1
  
  
  
#Andiamo a fare con un piccolo menu   
  
 
# variabile del menu   
x = input( "digita qualcosa" )
#  menu di cambiamento X
while( x != " esci "): 
   scelta = ""
   print( " 1 - cambia , 2 - esci , 3 - rimani  " )
   scelta = input( " Inserisci la tua scelta tramite numero " )
   if( scelta == 1  ):
     x = "cambia"
     break
   if( scelta == 2 ):
     x =  " esci "
   if( scelta == 3   ):
     x = " nulla "
   else:
     print( "scelta sbagliata riprovare" )
     continue
else:
   x = "c'è stato un errore"
   
   
if( x == "cambia"): 
   print("hai finito")
elif ( x == "esci"  ):
   print(" hai sbagliato riprova ")
else: 
   print (" qualcosa è andato storto" )
  
  
  
  
  
  
  
  
  
  

  
    

UnDizionario = {
  "Brand": "Fiat",
  "Modello": "Tesla",
  "Anno": 2000
}

#I dizionari vengono utilizzati per memorizzare i valori dei dati in coppie chiave:valore

cars = ["Ford", "Volvo", "BMW"]

#Un arrays, la primsa posizione di un array e contata a aprtire da 0

x = cars[0]

print(x)