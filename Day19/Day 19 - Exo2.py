#Jouons avec les Sombres étiquettes
print("Exercice : Sombre Etiquettes, N'importe quel ordre !")

#Définition de la Fonction
def oiseau(voltage=100, etat='allumé', action='danser la Java'):
    print('Ce perroquet ne pourra pas', action)
    print('si vous le branchez sur', voltage, 'volts !')
    print("L'auteur de ceci est complètement", etat) 

#Appel de la Fonction en Fournissant des paramètres personnalisés
oiseau(action='programmer en Haxel', etat='Parano', voltage=500)

print()

#Appel de la Fonction sans Fournir de paramètres
oiseau()