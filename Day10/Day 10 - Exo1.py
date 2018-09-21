# Écrivez un programme qui convertisse en mètres par seconde une vitesse fournie par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
print("Exercice : Convertisseur de Vitesse")
nombre = input("Veuillez entrer la vitesse à laquelle vous roulez : ")
vitesse = int(nombre)
print("Vous avez saisi la vitesse", vitesse, "miles/heure")
vitesseMetreSconde = (vitesse*1609)/3600
print("Elle équivaut en mètres par seconde", vitesseMetreSconde, "m/s")
    #Tout ceci parait Izi, Jusqu'ici Tout va Bien X) !