#Déterminer si une année (dont le millésime est introduit par l’utilisateur) est bissextile ou non. Une année A est bissextile si A est divisible par 4. Elle ne l’est cependant pas si A est un multiple de 100
print("Exercice :  Bisextile ou Pass, Heunn ?")
anneeSaisie = int(input("Veuillez saisir une année quelconque : "))
if(anneeSaisie%4 == 0):
    print(anneeSaisie, "est une annee Bissextile Heun !")
else:
    if(anneeSaisie%100 == 0):
        print(anneeSaisie, "n'est pas Bissextile")
    else:
        print("Aucun des deux En fait !")
print("Aurevoir Merci !")