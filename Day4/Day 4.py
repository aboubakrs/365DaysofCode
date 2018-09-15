#Exercice : Verifions s'il nous reste beaucoup de Joukh pour 365DaysofCode
actualDay = 4

if(actualDay < 365):
    print("T'es encokh Loin Frekhee X)...")
else:
    print("Bah Bravoo Morray, Tu y es Presque...")


#Exercice : Echauffement avec les opérateurs de comparaison
heure_actuelle = "19h50mn45s"

if(heure_actuelle != "20h30mn00s"):
    print("C'est pas encore l'heure de prier Guew")
else :
    print("Guew deih Diot neu Baye Hahaha, Diougueul Diouli !!")


#Exercice : Echauffement avec les annimaux du Bendo... Instructions Imbriquées
embranchement = "vertebres"
classe = "mammiferes"
ordre = "carnivores"
famille = "felins"

if embranchement == "vertebres":
    if classe == "mammiferes":
        if ordre == "carnivores":
            if famille == "felins":
                print("It's maybe a Ninja Cat'zer")
        print("Fall, c'est en tout cas un Mammifère")
    elif classe == "oiseaux":
        print("C'est maybe un Canari, Mais oui Mais oui c'est bien un canari")
print("Laisse tomber wallah la Classification des animaux est complexe")
