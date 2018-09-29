#Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca. 
print("Exercice : Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca. ")

#Définition de la Fonction
def ligneCar(n, ca):
    chaine=""
    while(n>0):
        chaine += str(ca)
        n = n - 1
        if(n == 0):
            return chaine

#Testons la Fonction
print("La chaine de caractères formée : ", ligneCar(3, "Sal"))

    #Instructions conditionnelles et Fonctions n'ont plus de secret pour moi X) !