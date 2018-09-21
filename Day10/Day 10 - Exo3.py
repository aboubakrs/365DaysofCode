#Écrivez un programme qui calcule la période d’un pendule simple de longueur donnée
from math import *

print("Exercice : Les lois de la Physique Zer")
longueur = float(input("Indiquez en metre la longueur du Pendule : "))
print("Longueur =", longueur, "m")
g = 9.8
print("La valeur de l'accélération de la pesanteur sur Terre =", g, "N/kg")
T = (2*pi)*(sqrt(longueur/g))
print("La période d'un pendule simple de longueur", longueur, "m =", T )
    #Simple Amusement en Physique Hahaa X)