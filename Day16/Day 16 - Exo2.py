#Test de notre module de Foctions dessins_tortue
print("Exercice : Dessins de 10 carres Rouges en utilisant le module de Fonction dessins_tortue")

from dessins_tortue import *

up()            #Relever le crayon
goto(-150, 50)  #Se placer sur le point de Coordonnees x=-150 et y=50

#L'instruction up() était necessaire avant l'instruction goto() sinon on allait se dplacer en dessinant alors que c'est pas ce qu'on veut

#Dessinons 10 carres rouges à l'aide de la fonction carre() du module dessins_tortue
i = 0
while(i<10):
    down()           #Abaisser le Crayon
    carre(25, 'red') #Tracer un carre
    up()             #Relever le crayon
    forward(30)      #Avancer plus loin
    i = i + 1
a = input()          #Ca ne fait rien, juste pour mettre la fenetre en pause