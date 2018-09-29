#Définissez une fonction inverse(ch) qui permette d’inverser les l’ordre des caractères d’une chaîne quelconque. La chaîne inversée sera renvoyée au programme appelant.
print("Exercice : Inversion de Chaine")

#Définition de la Fonction
def inverse(ch):
    chaine = str(ch)
    longChaine = len(chaine)-1
    chaineInversee = ""
    while(longChaine >= 0):
        if(chaine[longChaine]):
            chaineInversee += chaine[longChaine]
        longChaine = longChaine - 1
    return chaineInversee


#Testons la Fonction
print(inverse("Booba Yaffa Luna Yaffa Omar Yaffa"))