
# x = 19     # global scope  \  ambito globale 

def Pippo():
    y = 11   # local scope  \  ambito locale
    #print(y)
    global x 
    x = 100
    print(x)
 

def Pippo2():
    y = 11   # local scope  \  ambito locale
    #print(y)
    
    x = 200
    print(x)
    
    
Pippo()
print(x)
Pippo2()
print(x)