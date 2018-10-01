#Modifiez la fonction volBoite(x1,x2,x3) que vous avez définie dans un exercice précédent, de manière à ce qu’elle puisse être appelée avec trois, deux, un seul, ou même aucun argument. Utilisez pour ceux ci des valeurs par défaut égales à 10.
print("Exercice : Volume boite Parallelepipede")

#Definition de la Fonction
def volBoite(x1=10.0, x2=10.0, x3=10.0):
    return (x1*x2*x3)

#Appel de la Fonction sans paramètres
print("Le volume de la boite est : ", volBoite(), "mètre cube")
print()

#Appel de la Fonction en Fournissant qu'un paramètre
print("Le volume de la boite est : ", volBoite(x1=5.2), "mètre cube")
print()

#Appel de la Fonction en Fournissant que deux paramètres
print("Le volume de la boite est : ", volBoite(x1=5.2, x2=3), "mètre cube")
print()

#Appel de la Fonction en Fournissant les trois paramètres
print("Le volume de la boite est : ", volBoite(x1=20, x2=4.5, x3=2.0), "mètre cube")
print()