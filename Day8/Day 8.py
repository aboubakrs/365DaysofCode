#Écrivez un script qui détermine si une chaîne contient ou non le caractère « e »
print("Exercice : Script déterminant si une chaine contient ou non le caractere e...")
chaineDeCaractere = "Mister Kopp Hello"
for i in chaineDeCaractere:
    if(i == "e"):
        print("Cette chaine de caratere contient le caractere <<e>>")


print()
print()


#Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne. 
print("#Exercice : Script comptant le nombre d'occurences du caractere e dans une chaine")
chaine = "Si le monde est à moi, le monde est à nous, Scarfaceeeee. Les autres en Face sont Jalouxxx !!"
compteurE = 0
for z in chaine:
    if(z == "e"):
        compteurE = compteurE + 1
print("Le nombre de <<e>> trouvrés dans cet chaine = ", compteurE)


print()
print()


#Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères. 
print("Exercice : Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères. ")
variableCourante = "BoobaBrazza92i"
nouvelleVariable = ""
for i in variableCourante:
    nouvelleVariable = i + "*"
    print(nouvelleVariable, end="")


print()
print()


#Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant
print("Exercice : Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant")
variableAncienne = "Luna et Omar Yaffa"
variableLongueur = len(variableAncienne) - 1
variableNouvelle = ""
while(variableLongueur >= 0):
    variableNouvelle = variableAncienne[variableLongueur]
    variableLongueur = variableLongueur - 1
    print(variableNouvelle, end="")

#C'etait du Gateau, c'etait intekhessant de Jouer avec les Indices'zer Mais J'ai quand meme
#Trimer Pouloulouuuuu. Ca m'a secoué les ménongesss !!!! X)