# Définissez une fonction eleMax(liste,debut,fin) qui renvoie l’élément ayant la plus grande valeur dans la liste transmise. Les deux arguments debut et fin indiqueront les indices entre lesquels doit s’exercer la recherche, et chacun d’eux pourra être omis (comme dans l’exercice précédent). 
print("Exercice : Max n'est pas forcément le Max")

#Définition de la Fonction
def eleMax(liste, debut=0, fin=-1):
    if(fin == -1):
        fin = len(liste)-1
    maxi = 0
    i = 0
    while(i <= len(liste)-1):
        if( i>=debut and i<=fin and liste[i]>maxi):
            maxi = liste[i]
        i = i + 1
    return maxi

#Test de la Fonction
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2] 
print(serie)
print()

print(eleMax(serie))
print()

print(eleMax(serie, 2, 5))
print()

print(eleMax(serie, 2))
print()

print(eleMax(serie, fin =3, debut =1)) 
print()