#Valeurs Par Défaut pour les paramètres
print("Exercice : Valeurs par défaut pour les paramètres")

#Définition de la Fonction
def question(annonce, essais =4, please ='Oui ou non, s.v.p.!'):
    while(essais>0):
        reponse = input(annonce)
        if reponse in ('o', 'oui', 'O', 'Oui', 'OUI'):
            return 1
        if reponse in ('n', 'non', 'N', 'Non', 'NON'):
            return 0
        print(please)
        essais = essais-1

#Testons la Fonction
question('Voulez-vous vraiment terminer ? ')

#Commentaire !!!
"""
    Ce que ce programme fait lorsqu'on l'éxecute, c'est qu'il demande d'abord
    si on veut vraiment terminer ?...
        - Si l'utilisateur saisit o ou O ou oui ou Oui ou encore OUI. Le programme
            retourne 1 et tout se passe bien.
        - Si l'utilisateur saisit n ou N ou non ou Non ou encore NON. Le programme
            retourne 0 et tout se passe bien.
        - Si l'utiliateur saisit autre chose, le programme de saisir oui ou non, svp
            en l'accordant 4 essais. Si les 4 essais sont épuisés, le programme met 
            fin à son fonctionnement.
"""