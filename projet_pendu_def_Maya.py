def menu():
    """fonction menu qui permet de structurer le programme en appelant les différentes fonctions"""
    print("JEU DU PENDU","\n")
    motchoisi=choixmot()
    taille=(len(motchoisi)-1) #taille du mot choisi sans le retour à la ligne
    #print(taille)

    motatrouver=[]
    for i in range (taille):
        motatrouver.append ("-")  #met des tirés qui correspondent au nombre de lettres que contient le mot choisi
    #print(motatrouver)
    traits = "".join(motatrouver) #transformer le tableau motatrouver en str
    print(traits,"\n")
    #print(type(motatrouver))
    #print(type(traits))
    pendu=0 #initialiser un compteur pour le pendu
    lettredejaprop=[] # initialiser un tableau contenant les lettre deja proposées
    while pendu !=6 and traits != motchoisi : #création d'une boucle while pour que le jeu s'arrete lorsque le pendu est complet ou que le mot est trouvé
        lettrechoisi=choixlettre()
        #print("lettre choisie ", lettrechoisi)
        pendu,motatrouver =verif(lettrechoisi,motchoisi,lettredejaprop,motatrouver,pendu)
        #print(pendu)
        traits = "".join(motatrouver)+"\n" #transformer list en str pour un plus joli rendu
        print(traits) #affiche les traits et les lettres trouvées dans le mot
    if pendu==6:
        print("Désolé, c'est perdu, le mot était ",motchoisi) #affiche que le joueur a perdu
    else:
        print("Bravo vous avez gagné") #affiche que le joueur a gagné

def dessinPendu(nb):
    """fonction qui permet de dessiner le pendu"""
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]

def choixmot():
    """choisis un mot au hassard parmis les 835 du fichier texte, et le renvoie"""
    with open ("dico.txt","r") as fichier : #ouvrir le fichier txt contenant les 835 mots
        id=[] #créer un tableau vide
        for i in fichier:
            id.append(i) #ajouter tous les mots du fichier dans le tableau id
        longueur=len(id)
        #print(id)
        #print(longueur)
        motchoisi=id[randint(1,longueur)]#choisir un mot au hasard dans le tableau de 835 mots
        #print(motchoisi)
        return motchoisi

def choixlettre():
    """fonction qui permet de laisser le joueur entrer une lettre, et la renvoie"""
    lettrechoisi=input("Proposez une lettre : ") #l'utilisateur entre une lettre
    return lettrechoisi.upper() #la lettre entrée est mise en majuscule

def verif(lettrechoisi,motchoisi,lettredejaprop,motatrouver,pendu):
    """fonction qui verifie que la lettre entrée fasse partie du mot choisi, renvoie le compteur 'pendu' et l'évolution du mot 'motatrouver' """
    if lettrechoisi in motchoisi : #verifie si la lettre fait partie du mot choisi
        print("Cette lettre est correcte")
        if lettrechoisi in lettredejaprop: #verifie si la lettre a deja était dite
            print("Faites attention, vous avez déjà proposé cette lettre !")
        else:
            lettredejaprop.append(lettrechoisi) #ajouter la lettre entrée dna sle tableau des lettres déjà dites
        print(dessinPendu(pendu)) #affiche le dessin du pendu
        #print(lettredejaprop)

        for i in range (len(motchoisi)-1):
            if lettrechoisi==list(motchoisi)[i]:
                #print("lettre en position ", i )
                motatrouver[i]=lettrechoisi #remplace le(s) tiré(s) correspondant(s) à l'emplacement de la lettre dans le mot choisi par la lettre entrée
            i=i+1
        #print(motatrouver)

    else:
        print("Cette lettre est incorrecte")
        if lettrechoisi in lettredejaprop: #verifie si la lettre a deja était dite
            print("En plus, vous avez déjà proposé cette lettre !")
        else:
            lettredejaprop.append(lettrechoisi) #ajouter la lettre entrée dna sle tableau des lettres déjà dites
        pendu=pendu+1
        print(dessinPendu(pendu)) #affiche le dessin du pendu
        #print(lettredejaprop)

    return pendu, motatrouver



from random import*
menu()
