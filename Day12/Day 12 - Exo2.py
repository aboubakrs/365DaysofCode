#Demander à l’utilisateur son nom et son sexe (M ou F). En fonction de ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne. 
print("Exercice :  Eufichage")
nom = input("Bonjour, Veuillez saisir votre nom pour commencer : ")
sexe = input("Indiquez votre Sexe en saisissant M pour masculin ou F pour féminin : ")
if(sexe == "M"):
    print("Merci Cher Monsieur", nom, ",Aurevoir Merci !")
else:
    if(sexe == "F"):
        print("Merci Chère Mademoiselle", nom, ",Aurevoir Merci !")
    else:
        print("Le sexe que vous avez indiqué est Invalide !")
