thisset = {"apple", 21, "cherry" }
print(thisset)
print(len(thisset))
print(type(thisset))

thisset2 = set(("apple", "banana", "cherry")) # double round-brackets
print(thisset2)

for x in thisset:
    print(x)
    
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)    # andiamo ad unirre più valori dei nostri set assieme
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)     # andiamo a trovare le referenze in comune ai set

print(x)