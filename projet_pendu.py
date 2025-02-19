def menu():
    """fonction menu qui permet de structurer le programme en appelant les différentes fonctions"""
    print("JEU DU PENDU","\n")
    motchoisi=choixmot()
    taille=(len(motchoisi)-1) #taille du mot choisi sans le retour à la ligne
    #print(taille)
    motatrouver=[]
    for i in range (taille):
        motatrouver.append ("-")  #met des tirés à la place de chaque lettre du mot choisi
    #print(motatrouver)
    traits = "".join(motatrouver)#transformer list en str
    print(traits,"\n")
    #print(type(motatrouver))
    #print(type(texte))
    pendu=0 #initialiser un compteur pour le pendu
    lettredejaprop=[] # initialiser un tableau contenant les lettre deja proposées
    while pendu !=6 and traits != motchoisi.lower():
        lettrechoisi=choixlettre()
        pendu =verif(lettrechoisi,motchoisi,lettredejaprop,pendu)
        #print(pendu)
        #print(traits)
        traits = "".join(motatrouver)#transformer list en str
        print(traits,"\n")
    if pendu==6:
        print("Désolé, c'est perdu, le mot était ",motchoisi)
    else:
        print("Bravo vous avez gagné")

def dessinPendu(nb):
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
    """choisis un mot au hassard parmis les 800 du fichier texte et le renvoie"""
    with open ("dico.txt","r") as fichier : #ouvrir le fichier txt contenant les 835 mots
        id=[] #créer un tableau vide
        for i in fichier:
            id.append(i) #ajouter tous les mots du fichier dans le tableau id
        longueur=len(id)
        #print(longueur)
        motchoisi=id[randint(1,longueur)]#choisir un mot au hasard dans le tableau de 835 mots
        print(motchoisi)
        return motchoisi

def choixlettre():
    """le joueur choisi une lettre"""
    lettrechoisi=input("Proposer une lettre : ") #l'utilisateur entre une lettre
    return lettrechoisi

def verif(lettrechoisi,motchoisi,lettredejaprop,pendu):
    if lettrechoisi in motchoisi.lower(): #verifie si la lettre fait partie du mot choisi
        print("Cette lettre est correcte")
        if lettrechoisi in lettredejaprop: #verifie si la lettre a deja était dite
            print("Faites attention, vous avez déjà proposé cette lettre !")
        else:
            lettredejaprop.append(lettrechoisi)
        print(dessinPendu(pendu))
        print(lettredejaprop)

        #taille=(len(motchoisi)-1) #taille du mot choisi sans le retour à la ligne
        #print(taille)
        #motatrouver=[]
        #for i in range (taille):
        #    motatrouver.append ("-")  #met des tirés à la place de chaque lettre du mot choisi
        #print(motatrouver)
        #for lettrechoisi in motchoisi:
        #    motatrouver[i]=lettrechoisi
        #traits = "".join(motatrouver)#transformer list en str
        #motatrouver[motchoisi[lettrechoisi]]=lettrechoisi
        #motatrouver

        #traits = "".join(motatrouver)#transformer list en str
        #print(traits,"\n")


    else:
        print("Cette lettre est incorrecte")
        if lettrechoisi in lettredejaprop: #verifie si la lettre a deja était dite
            print("En plus, vous avez déjà proposé cette lettre !")
        else:
            lettredejaprop.append(lettrechoisi)
        pendu=pendu+1
        print(dessinPendu(pendu))
        #print(lettredejaprop)

        #traits = "".join(motatrouver)#transformer list en str
        #print(traits,"\n")

    return pendu



from random import*
menu()
