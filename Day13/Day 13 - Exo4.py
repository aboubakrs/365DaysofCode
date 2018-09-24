#Les Fonctions avec Paramètres !
print("Exercice : C'est ma Premiere Fonction avec Parametre")

#Définition Fonction
def tableMultiplication(inVariant):
    print("La table de Multiplication par ", inVariant)
    n = 1
    while(n <11):
        print(inVariant, "*", n, "=", inVariant*n)
        n = n + 1

#Utilisation d'une variable saisie par le User
a = int(input("Veuillez saisir un nom pour lequel vous souhaitez la Table de Multiplication : "))

#Appel de la fonction
tableMultiplication(a)