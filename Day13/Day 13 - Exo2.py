#Ca joue un peu avec les fonctions
print("Exercice : C'est ma première Fonctionkh Simple !")

#Définition d'une Fonction
def tableMultiplicationPar7():
    n = 1
    while(n < 11):
        print(7, "*", n, "=", n*7)
        n = n + 1


#Reutilisation de Fonctions Originales
def tableMultiplicationPar7Trple():
    print("La table de Multiplication par 7 en Triple Exemplaire")
    tableMultiplicationPar7()
    tableMultiplicationPar7()
    tableMultiplicationPar7()

#Appel de la Fonction
tableMultiplicationPar7Trple()