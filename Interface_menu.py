from ezTK import *
from Drop import *
from Interface_game import *
from Interface_scores import *
from Tkinter import *
# ------------------------------------------------------------------------------

#fonction de création de la grille de Drop par-dessus l'interface menu 

root=Tk()
root.configure(width=200,height=100)
root.mainloop()
#Je ne sais pas encore exactement comment l'utiliser, mais normalement c'est fait pour redimensionner la taille
#de la fenêtre comme on veut avec Tkinter
# Voilà le lien si tu veux : https://www.developpez.net/forums/d28285/autres-langages/python-zope/gui/tkinter/tkinter/

class Interface_menu(Win):

    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=3):

        Win.__init__(self, title='DROP', bg=('#cde3f2'),op=10)
        # trouver comment donner une taille fixe à la fenêtre 

        self.nbBricks = nbNewBricks
        self.varSize = size
        self.rows = rows
        self.cols = cols
        self.name = StringVar(self,'Anonyme')

        Topframe = Frame(self, fold = 1)
        Label(Topframe, text="BIENVENUE SUR LE DROP", font='Cambria 30', bg="#cde3f2", relief ="groove", op = 10)

        Midframe = Frame(self, fold = 2, height = 9)
        Label(Midframe, text="Tout d'abord, entrez votre nom de joueur /n", font='Cambria 13', width="30", bg="#cde3f2", relief ="groove")
        self.nameEntry = Entry(Midframe,textvariable=self.name, font='Cambria 13', width="15", bg="#cde3f2")
        #Il faut que le nom soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        #message d'erreur si il n'y a pas de pseudo

        self.gridSize = Label(Midframe, text="Sélectionnez le format de grille avec lequel vous souhaitez jouer /n", font='Cambria 13', width="9", bg="#cde3f2")
        liste = Listbox(Midframe)
        liste.insert(1, "8 lignes, 5 colonnes (défaut)")
        liste.insert(2, "16 lignes, 10 colonnes (maxi)")
        liste.insert(3, "8 lignes, 8 colonnes (carré)")
        liste.insert(4, "6 lignes, 3 colonnes (mini)")
        #Il faut que le paramètre sélectionné soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        #POURQUOI LA LISTE DEROULANTE S'AFFICHE PAS BIEN FJPOEIZOGBI

        self.newBricks = Label(Midframe, text="Combien de briques voulez-vous gérer par tour ?",  font='Cambria 13', width="9", bg="#cde3f2" )
        liste2 = Listbox(Midframe)
        liste2.insert(1, "Deux (défaut)")
        liste2.insert(2, "Trois")
        liste2.insert(3, "Quatre")

        self.play = Button(Midframe, text="Commencer à jouer",  font='Cambria 13', width="9", bg="#cde3f2", command = self.create_drop)
        #Il faut que le paramètre sélectionné soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        # quand on débute le jeu, on ouvre l'interface de jeu
        # si tous les paramètres de la grille sont pas remplis, message d'erreur ou utilisation de paramètres par défaut ? 

        Bottomframe = Frame(self, fold = 2)
        self.scores = Button(Bottomframe, text='Esprit compétitif ? Consultez le tableau des scores',  font='Cambria 10', width="9", bg="#cde3f2", command = Interface_scores)
        # tableau des scores dans un fichier texte ou excel ? -> texte (save.txt)
        self.regles = Button(Bottomframe, text='Besoin d\'aide ? Consultez les règles du jeu',  font='Cambria 10', width="9", bg="#cde3f2", command = Regles)
        # ouvre une fenetre ou les regles s'affichent tout simplement
        self.loop()

        # def play(self): 

        #     self.reset = Button(frame, text='RESET', width="9", bg="#CDCDCD", command= drop.reset)
        #     frameGrid
        #     self.brickcolor = ['#bf3f28', '#f19908', ' #feedce', '#85ec62', ' #62ecea ', ' #358ecb ', ' #2e429e ', ' #eb6ff3 ', ' #fc2737 ', '#000000']

        # #Création de la grille vide
        # self.grid = grid(self.rows, self.cols, 0)

        # self.frameGrid = Frame(self,fold=cols,op=3)
        # for n in range(cols * rows): Brick(self.frameGrid, width=size, height=size, bd=0)

        # self.reset()
        # #dans le tableau, si on est avant la ligne 4, alors la grille a la couleur du fond
        # #sinon la grille a la couleur de la zone jouable

        # #grille [x][-y] debut en haut a gauche
        # self.gridBricks = self[0]
        # # self.gridBricks[self.nbBricks-1][1]['bg'] = self.colors[2]
        # #deuxieme ligne deuxieme colonne : initiatisation d'une brique colorée a empiler
        # # self.gridBricks[self.nbBricks-1][2]['bg'] = self.colors[3]
        # # deuxieme ligne troisieme colonne : initiatisation d'une brique colorée a empiler

    def create_drop(self):
        self.name = self.nameEntry.get()
        if self.name == '' or not self.name.isalnum():
            self.name = 'Unknow'
        Interface_game(self.rows,self.cols,self.nbBricks,self.varSize,self.name)


class Regles(Win):
    def __init__(self):
        Win.__init__(self) 
        regles = "Le but du jeu est de former des assemblages d'au moins 3 blocs /n adjacents de la même couleur. Chaque fois qu'un tel assemblage /n"
        "est obtenu, il est remplacé par un bloc de plus haut niveau, /n caractérisé par une nouvelle couleur. /n"
        "Pour arriver à cela, vous devez réfléchir à la façon dont vous /n disposez les blocs dans la grille de jeu. Vous pouvez les /n"
        "faire pivoter ou les décaler sur toute la largeur de la grille. /n"
        "/n"
        "Votre score est calculé en fonction de la taille des assemblages /n et de la couleur des blocs assemblés. Alors ne lésinez pas /n"
        "sur la quantité... Mais n'oubliez pas que les blocs de haut /n"
        "niveau sont plus longs à obtenir ! " 
        self.txtend = Label(self, text=regles, font='Cambria 20', width="15", fg='#000000')

if __name__ == "__main__":
  # t = [(2,'r'),(4,'d'),(1,'k'),(2,'c')]
  # t.sort(reverse=True)
  # print(t)
  # g = grid(5,3,0)
  # for i in range(g.col): print(g[1,i])
  # # print(g)
  Interface_menu()
#Interface_game(6,5,3)