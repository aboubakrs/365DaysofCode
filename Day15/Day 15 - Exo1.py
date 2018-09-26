#Le monde des Variables Globales
print("Exercice : Le monde des Variables Globales")

#Définition de La Fonction
def variableGlobale():
    global seLever
    global marcher
    global courir
    seLever = seLever + 1
    marcher = marcher + 2
    courir = courir + 3
    print("La valeur de seLever : ", seLever)
    print("La valeur de marcher : ", marcher)
    print("La valeur de courir : ", courir)

#Testons en Affectant quelques valeurs aux variables
seLever = 92
marcher = 12
courir = 14

#Appel de la Fonction
variableGlobale()

#Rappellons la Fonction
variableGlobale()

    #Ok Ca marche, c'est interessant Tout ca, ca prends en compte l'ancien appel de la fonction
