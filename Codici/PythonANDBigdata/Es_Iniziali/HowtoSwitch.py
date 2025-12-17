


def Pippo():
 print("CIAO MASTER D")
  
  

Pippo()
Pippo()


def my_function(fname, fsurname):
  print(fname + "  " + fsurname )

my_function("Mirko", "cognome")
my_function("Io sono un argomento " , " io un all'atro ")

def switch(lang):
  while(lang != "esci"):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"
    elif lang == "esci":
        break
    else:
        continue

lang = "ok"
while(lang != "esci"):
  
    lang = input(  "inserisci elemento" )

    print(switch(lang))   
 


"""
Output: 
You can become a web developer.
You can become a backend developer.
You can become a mobile app developer
"""

# """
# Output: 
# You can become a web developer.
# You can become a backend developer.
# You can become a mobile app developer
# """