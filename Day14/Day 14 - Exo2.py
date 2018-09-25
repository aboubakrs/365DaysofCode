#Les Fonctions avec plusieurs parametres
print("Exercice : Fonctions avec plusieurs paramètres / Interaction avec User")

#Définition de la Fonction
def tableMulti(invariant, debutMultiplication, finMultiplication):
    print("La table de multiplication par ", invariant, ":")
    n = debutMultiplication
    while(n <= finMultiplication):
        print(invariant, "x", n, "=", invariant*n)
        n = n + 1

#Utilisation d'une variable saisie par le User
a = int(input("Veuillez saisir un nombre pour lequel vous souhaitez la Table de Multiplication : "))
b = int(input("Saisissez ensuite un nombre de début : "))
c = int(input("Et enfin un nombre de Fin : "))

#Appel de la Fonction
tableMulti(a, b, c)

    #Aight Pas Mallllllllllllll