#Les Fonctions avec plusieurs parametres
print("Exercice : Fonctions avec plusieurs paramètres")

#Définition de la Fonction
def tableMulti(invariant, debutMultiplication, finMultiplication):
    print("La table de multiplication par ", invariant, ":")
    n = debutMultiplication
    while(n <= finMultiplication):
        print(invariant, "x", n, "=", invariant*n)
        n = n + 1

#Appel de la Fonction
tableMulti(8,0,30)