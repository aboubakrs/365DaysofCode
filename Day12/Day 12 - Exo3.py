#Demander à l’utilisateur d’entrer trois longueurs a, b, c. À l’aide de ces trois longueurs, déterminer s’il est possible de construire un triangle. Déterminer ensuite si ce triangle est, isocèle, équilatéral ou quelconque.
print("Exercice : Jouons avec les triangles")
a = int(input("Veuillez attribuer à 'a' une longueur quelconque : "))
b = int(input("Attribuez ensuite à 'b' une longueur : "))
c = int(input("Attribuez enfin à 'c' une longueur : "))
if((a<=0) | (b<=0) | (c<=0)):
    print("Il n'est pas possible de construire un triangle avec ces valeurs.")
else:
    print("Il est possible de construire un triangle avec ces valeurs.")
    if((a==b) & (c==b)):
        print("Et la nature de ce triangle est un : TRIANGLE EQUILATERAL")
    elif ( ((a==b) & (c!=b)) | ((a==c) & (c!=a)) | ((b==c) & (c!=a)) ):
        print("Et la nature de ce triangle est un : TRIANGLE ISOCELE")
    else:
        print("Et la nature de ce triangle est un : TRIANGLE QUELCONQUE")