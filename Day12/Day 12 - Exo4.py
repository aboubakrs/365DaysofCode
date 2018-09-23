#Demander à l’utilisateur qu’il entre un nombre. Afficher ensuite : soit la racine carrée de ce nombre, soit un message indiquant que la racine carrée de ce nombre ne peut être calculée. 
print("Exercice : Racine ou Carré ou pas ?")

from math import *

nombre = int(input("Veuillez saisir un nombre positif : "))
if(nombre < 0):
    print(nombre ,"est négatif, Impossible de calculer sa racine carrée")
else:
    print("La racine carrée du nombre", nombre, "vaut : ", sqrt(nombre))