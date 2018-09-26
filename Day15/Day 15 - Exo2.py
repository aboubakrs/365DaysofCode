#Les Vraies Fonctions, Tres Vraies, Pas comme les Procedures
print(" Les Vraies Fonctions, Tres Vraies, Pas comme les Procedures ")

#Définition de la Fonction
def tableMultiplication(inVariant):
    print("La table de Multiplication par ", inVariant)
    resultat = []
    n =1
    while(n <11):
        ligne = inVariant*n
        resultat.append(ligne)
        n = n +1
    return resultat

#Apple de la Fonction
tableTest = tableMultiplication(5)
print(tableTest)