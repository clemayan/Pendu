def menu():
    """fonction menu qui permet de structurer le programme en appelant les différentes fonctions"""
    print("JEU DU PENDU","\n")
    motchoisi=choixmot()
    taille=(len(motchoisi)-1) #taille du mot choisi snas le retour à la ligne
    #print(taille)
    for  i in motchoisi:
        motatrouver=["-"*taille] #met des tirés à la place de chaque lettre du mot choisi
        #print(motatrouver)
    traits = "".join(motatrouver)#transformer list en str
    print(traits,"\n")
    #print(type(motatrouver))
    #print(type(texte))
    lettredejaprop=[]
    pendu=0
    while pendu !=6 or traits != motchoisi.lower():
        lettredejaprop=lettredejaprop
        penud=pendu
        lettrechoisi=choixlettre()
        verif(lettrechoisi,motchoisi)
        print(traits)
    #tab=dessinPendu(6)

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

pendu=0
while pendu !=6 or traits != motchoisi.lower():
    lettredejaprop=[]
    pendu=0
    def choixlettre():
        """le joueur choisi une lettre"""
        lettrechoisi=input("Proposer une lettre : ") #l'utilisateur entre une lettre
        return lettrechoisi

    def verif(lettrechoisi,motchoisi):
        lettredejaprop=[] #création d'un tableau contenant les lettres deja proposées
        pendu=0
        if lettrechoisi in motchoisi.lower(): #verifie si la lettre fait partie du mot choisi
            print("Cette lettre est correcte")
            if lettrechoisi in lettredejaprop: #verifie si la lettre a deja était dite
                print("Faites attention, vous avez déjà proposé cette lettre !")
            else:
                lettredejaprop.append(lettrechoisi)
                pendu=pendu
                print(dessinPendu(pendu))
                print(lettredejaprop)
                #motatrouver[lettrechoisi in motchoisi]=lettrechoisi TRIUVER..
                texte = "".join(lettredejaprop)
                print(texte)

        else:
            print("Cette lettre est incorrecte")
            pendu=pendu+1
            if lettrechoisi in lettredejaprop: #verifie si la lettre a deja était dite
                print("En plus, vous avez déjà proposé cette lettre !")
            else:
                lettredejaprop.append(lettrechoisi)
                print(dessinPendu(pendu))
                #print(traits)
                #print(lettredejaprop)
    lettrechoisi=choixlettre()
from random import*
menu()
verif(lettrechoisi,motchoisi)
print(traits)
