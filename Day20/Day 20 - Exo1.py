#Modifiez la fonction volBoite(x1,x2,x3) ci-dessus de manière à ce qu’elle puisse être appelée avec un, deux, ou trois arguments. Si un seul est utilisé, la boîte est considérée comme cubique (l’argument étant l’arête de ce cube). Si deux sont utilisés, la boîte est considérée comme un prisme à base carrée (auquel cas le premier argument est le côté du carré, et le second la hauteur du prisme). Si trois arguments sont utilisés, la boîte est considérée comme un parallélépipède
print("Exercice : Encore la Boite de Pendor")

#Definition de la Fonction
def volBoite(x1=-1, x2=-1, x3=-1):
    if(x1 == -1 & x2 == -1 & x3 == -1): #Si aucun argument n'est fourni
        return -1
    elif(x1 != -1 & x2 == -1 & x3 == -1): #Si un seul argument est fourni
        return x1*x1*x1
    elif(x1 != -1 & x2 != -1 & x3 == -1): #Si deux arguments sont fournis
        return x1*x1*x2
    elif(x1 != -1 & x2 != -1 & x3 != -1): #Si les trois arguments sont fornuis
        return x1*x2*x3

#Appel de la Fonction sans paramètres
print("Appel de la Fonction sans paramètres.")
print(volBoite(), "! Erreur Survenue !")
print()

#Appel de la Fonction en Fournissant qu'un paramètre
print("Appel de la Fonction avec un seul paramètre.")
print("La boîte est Cubique et son Volume vaut : ", volBoite(5.2), "mètre cube")
print()

#Appel de la Fonction en Fournissant deux paramètres
print("Appel de la Fonction avec deux paramètres.")
print("La boîte est un Prisme à Base Carrée et son Volume vaut : ", volBoite(5.2, 3), "mètre cube")
print()

#Appel de la Fonction en Fournissant trois  paramètres
print("Appel de la Fonction avec trois paramètres.")
print("La boîte est un Parallélépipède et son Volume vaut : ", volBoite(5, 3, 7), "mètre cube")
print()