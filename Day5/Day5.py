#Jouons avec la Suite de Fibonacci, Suite dont chaque nombre = somme des deux nombres qui le précédent
a, b, c = 1, 1, 1
while(c < 11):
    print(b, end=" ")
    a, b, c = b, a+b, c+1


#Exercice : Ecrire un programme qui effectue la table de multiplication de 7
print()
print("La table de Multiplication de 7 : ")
nombreAmultiplier = 7
nombreVariant = 0
while(nombreVariant < 21):
    print(nombreAmultiplier, "x", nombreVariant, "=", nombreAmultiplier*nombreVariant)
    nombreVariant = nombreVariant + 1
    #Woulahh C'était facile mdr X)... Python is Awesome


#Exercice : Ecrire un programme qui affiche une table de conversions de somme d'argent
print()
print("Conversion Euro ---> Dollar Canadien")
nombreEnEuro = 1
nombreEnDollar = 1.65
while(nombreEnEuro <= 16384):
    print(nombreEnEuro, "euro(s) = ", nombreEnDollar, "dollar(s)")
    nombreEnEuro = nombreEnEuro * 2
    nombreEnDollar = nombreEnDollar * 2
    #Basiqueee X)


#Exercice :  Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au triple du terme précédent
print()
print("Suite de 12 nombres dont chaque Terme égale au triple du précédent")
nombreZer = 0.5
compteur = 0
while(compteur <= 12):
    print(nombreZer, end=" ")
    nombreZer = nombreZer**3
    compteur = compteur+1
    #I Swear Python is Awesome, Im Handling all these Exercises Well... Algo OKLM

