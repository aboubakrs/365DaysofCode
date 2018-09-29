# Définissez une fonction compteCar(ca,ch) qui renvoie le nombre de fois que l’on rencontre le caractère ca dans la chaîne de caractères ch
print("Exercice : Le nombre d'occurences d'un Caractère dans une Phkhase")

#Définition de la Fonction
def compteCar(ca, ch):
    carac = str(ca)
    chaine = str(ch)
    nbrcarac = 0
    for i in chaine:
        if i == carac:
            nbrcarac = nbrcarac + 1
    return nbrcarac


#Tester Fonction
print(compteCar("e", "Cette phrase est un exemple"))