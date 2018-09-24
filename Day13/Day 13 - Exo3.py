#Les Fonctions avec Paramètres !
print("Exercice : C'est ma Premiere Fonction avec Parametre")

#Définition Fonction
def tableMultiplication(inVariant):
    print("La table de Multiplication par ", inVariant)
    n = 1
    while(n <11):
        print(inVariant, "*", n, "=", n*inVariant)
        n = n + 1

#Appel de la Fonction
tableMultiplication(5)
tableMultiplication(13)
tableMultiplication(20)

#C'est Facile Tout ça, Jusqu'ici Tout va Biennn
