#Toujours avec les fonctions... Structuration d'un programme
print("Exercice : Fonctions et Programme Principal")

#Fonction retournant le cube d'un nombre
def cubeNombre(nombre):
    return nombre**3

#Fonction retournant le volume du sphère
def volumeSphere(rayon):
    return (4 * 3.14 * cubeNombre(rayon))/3

#Programme principal
print("Bienvenue dans notre programme de calcul du volume du Sphère !")
nombreSaisie = float(input("veuillez Saisir la Valeur du Rayon : "))
print("Le volume du Sphère de rayon", nombreSaisie, "vaut : ", volumeSphere(nombreSaisie))

