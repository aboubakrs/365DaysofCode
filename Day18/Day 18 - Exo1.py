#ez une fonction indexMax(liste) qui renvoie l’index de l’élément ayant la valeur la plus élevée dans la liste transmise en argument
print("Exercice : l'indice du maximum Maximum dans une liste")

#Définition de la Fonction
def indexMax(liste):
    laListe = list(liste)
    indexListe = 0
    while( indexListe <= (len(laListe)-1) ):
        if(laListe[indexListe] == max(laListe)):
            return indexListe
        indexListe = indexListe + 1

#Exemple, Testons la Fonction
Paris = [99, 93, 94, 95, 96, 97, 108]
print(indexMax(Paris))

    #l'algorithme m'a rendu un Peu Foukhhh !!