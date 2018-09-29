# Définissez une fonction nomMois(n) qui renvoie le nom du énième mois de l’année.
print("Exercice : Quel mois de l'année")

#Définition de la Fonction
def nomMois(n):
    calendrier = ["Aucun mois", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    while(n>=0 & n<=12):
        return calendrier[n]

#Test de la Fonction
print(nomMois(12))