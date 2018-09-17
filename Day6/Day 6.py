#Écrivez un programme qui calcule le volume d’un parallélépipède rectangle dont sont fournis au départ la largeur, la hauteur et la profondeur. 
longueur = 25
largeur = 12
hauteur = 3
volumeParallelepipede = longueur * largeur * hauteur
print("Exercice : Soit un parallélipéde dont la Longueur = ", longueur, ", la Largeur = ", largeur, " et la Hauteur = ", hauteur)
print("Son volume est obtenue en multipliant Longueur x Largeur x Hauteur.")
print("Ainsi le Volume = ", longueur, "x", largeur, "x", hauteur, "=", volumeParallelepipede, "cm3")


print()
print()
#Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3. Exemple :   7   14   21 * 28   35   42 * 49 ..
print("Exercice : 20 premiers termes de la table de multiplication par 7")
nbrAmultiplier = 7
nbrVariant = 0
while(nbrVariant <= 20):
    print(nbrAmultiplier*nbrVariant, end=" ")
    nbrVariant = nbrVariant + 1
    if((nbrAmultiplier*nbrVariant)%3==0):
        print("*", end=" ")


print()
print()
#Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13, mais n’affiche que ceux qui sont des multiples de 7. 
print("Exercice :50 premiers termes de la table de multiplication par 13 ")
nombreAmultiplier = 13
nombreVariant = 0
while(nombreVariant <= 50):
    if((nombreAmultiplier*nombreVariant)%7==0):
        print(nombreAmultiplier*nombreVariant, end=" ")
    else :
        print("", end="")
    nombreVariant = nombreVariant + 1
    #Les expressions conditionnelles sont intekhessantes, ça prouve que tu maitrises l'algo haha X)


print()
print()
#Écrivez un programme qui affiche la suite de symboles suivante : Genre Sapin
print("Exercice : Programme Sapin")
maxLignes = 7
maxColonnes = 7
#__________________ A suivre _________________