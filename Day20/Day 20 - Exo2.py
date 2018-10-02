#Définissez une fonction changeCar(ch,ca1,ca2,debut,fin) qui remplace tous les caractères ca1 par des caractères ca2 dans la chaîne de caractères ch, à partir de l’indice debut et jusqu’à l’indice fin, ces deux derniers arguments pouvant être omis (et dans ce cas la chaîne est traitée d’une extrémité à l’autre). 
print("Exercice :  Remplacement de Caractères")

#Definition de la Fonction
def changeCar(ch, ca1, ca2, debut=0, fin=-1):
    if fin == -1:
        fin = len(ch)-1
    nouvCh = ""
    i = 0
    while(i <= len(ch)-1):
        if( i>=debut and i<=fin and ch[i]==ca1 ):
            nouvCh = nouvCh + ca2
        else:
            nouvCh = nouvCh + ch[i]
        i = i + 1
    return nouvCh

#Test de la Fonction
print(changeCar("Ceci est une toute petite phrase.", ' ', '*'))
print()
print(changeCar("Ceci est une toute petite phrase.", ' ', '*', 8, 12))
print()
print(changeCar("Ceci est une toute petite phrase.", ' ', '*', 12))
print()
print(changeCar("Ceci est une toute petite phrase.", ' ', '*', fin=12))