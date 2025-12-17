# # Prime variabili


# a = 20
# b = 19




# #Primi blocchi: Condizioni ( IF per ora )


  
# testvero = True

# if (testvero !=False):  {
#   print(b+a)}
  
  
# if  testvero != False:    # controllo di negazione
  
#   testvero = False
#   if testvero == False: # controllo semplice
    
#     print("il tipo è")
    
# print( testvero )
  
  
#   # Un nuovo comando una nuova istruzione ovvero INPUT
  
  
# if (b > a):         # ( se.. )  if --> l'elemento di apertura della condizione 
#   print("b è più grande di a")
# elif (b == a) :     # ( invece se.. )  elif --> l'elemento di concate<nazione nelle condizioni composte
#   print("siamo uguali")
# else:
#   print("b non è più grande di a ne pari a lui")  
  
  
# n=int(input('digita un numero: ')) 

# if (n>0):
#   print('il numero è positivo') 
# else:
   
#   if (n==0): 
#     print('il numero è zero') 
#   else: 
#     print('il numero è negativo')
  
  

nv = 9

print(nv > 3 and nv > 10 and nv > 4) #il nostro operatore logico AND --> servirà a controllare conteporamente la veridicità di più condizioni 
                               #la dove se anche solo una, diviene meno, tutta la condizione false
                               
print(nv < 3 or nv > 10)       # servirà a controllare conteporamente la veridicità di più condizioni
                             #la dove solo una condizione, rimane true
# if (nv > 4):
#   { print( "è superiore ha 4")   }
# if (nv < 10):
#       { print (" è inferiore a 10" ) }
  
  
  
  
  
# c = 30
  
# # Variabili SEMANTICHE di if 
  
# if c > b: print("a is greater than b")  

# print("A") if a > b else print("B")