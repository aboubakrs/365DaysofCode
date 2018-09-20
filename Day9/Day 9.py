#Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant 
print("Exercice : Jouons avec le Calendriekh")
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
i1 = 0
i2 = 0
while((i1 <= 11) & (i2 <= 11)):
    t3.append(t2[i2])
    t3.append(t1[i1])
    i1 = i1 + 1
    i2 = i2 + 1
print(t3)
    #Tellement facile ces listes, Douma Sakh Nitt Woullah


print()
print()


#Écrivez un programme qui affiche « proprement » tous les éléments d’une liste. Si on l’appliquait par exemple à la liste t2 de l’exercice ci-dessus, on devrait obtenir
print("Exercice : Jouons encokh avec Ces sombres Calendriekhhhh en affichznt proprement les Listes")
c2 = 0
while(c2 <= 11):
    print(t2[c2], end=" ")
    c2 = c2 + 1
    #Fait en 45 secondes Tres Sombrement


print()
print()


#Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15]
print("Exercice : Affichage du plus grand nombre d'une liste")
maximum = [32, 5, 12, 8, 3, 75, 2, 15]
print("Le plus grand élément de cette liste a la valeur", max(maximum))
    #Wallah Je l'ai fait en 30 secondes, C'était Izi pour ne pas dire IZI X) !!! 


print()
print()


#Écrivez un programme qui analyse un par un tous les éléments d’une liste de nombres (par exemple celle de l’exercice précédent) pour générer deux nouvelles listes. L’une contiendra seulement les nombres pairs de la liste initiale, et l’autre les nombres impairs. Par exemple, si la liste initiale est celle de l’exercice précédent, le programme devra construire une liste pairs qui contiendra [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15]
print("Exercice : Les nombres Paikh et Impaikh")
nombre = [32, 5, 12, 8, 3, 75, 2, 15]
pair = []
impair = []
index = 0
while(index <= 7):
    if(nombre[index]%2 == 0):
        pair.append(nombre[index])
    else:
        impair.append(nombre[index])
    index = index + 1
print("La liste des nombres pairs est : ", pair)
print("La liste des nombres impairs est : ", impair)


print()
print()

# Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) pour générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères, l’autre les mots comportant 6 caractères ou davantage
print("Exercice : Longueukh des Noms du Bendo")
noms = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
moinsDeSix = []
sixEtPlus = []
indexNom = 0
while(indexNom <= 5):
    if(len(noms[indexNom]) < 6):
        moinsDeSix.append(noms[indexNom])
    else:
        sixEtPlus.append(noms[indexNom])
    indexNom = indexNom + 1
print("La liste des noms comportant moins de six caracteres : ", moinsDeSix)
print("La liste des noms comportant six ou plus de six caracteres : ", sixEtPlus)