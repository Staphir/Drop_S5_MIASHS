from ezTK import *
from Drop import *
# ------------------------------------------------------------------------------

#fonction de création de la grille de Drop par-dessus l'interface menu 

class Interface_menu(Win):

    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=3):

        Win.__init__(self, title='DROP', bg=('#cde3f2'),op=10)
        # trouver comment donner une taille fixe à la fenêtre 

        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.rows = rows
        self.cols = cols

        Topframe = Frame(self, fold = 1)
        Label(Topframe, text="BIENVENUE SUR LE DROP", font='Cambria 30', bg="#cde3f2", relief ="groove")

        Midframe = Frame(self, fold = 2)
        Label(Midframe, text="Tout d'abord, entrez votre nom de joueur", font='Cambria 14', width="30", bg="#cde3f2", relief ="groove")
        self.name = Entry(Midframe, font='Cambria 14', width="15", bg="#cde3f2")
        #Il faut que le nom soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        #message d'erreur si il n'y a pas de pseudo

        self.gridSize = Label(Midframe, text="Sélectionnez le format de grille avec lequel vous souhaitez jouer", font='Cambria 14', width="9", bg="#cde3f2")
        liste = Listbox(Midframe)
        liste.insert(1, "Prout (défaut)")
        liste.insert(2, "Prout")
        liste.insert(3, "Prout")
        liste.insert(4, "Prout")
        #Il faut que le paramètre sélectionné soit enregistré quand on lance le jeu (et aussi sur les scores ?)

        self.newBricks = Label(Midframe, text="Combien de briques voulez-vous gérer par tour ?",  font='Cambria 14', width="9", bg="#cde3f2" )
        liste2 = Listbox(Midframe)
        liste2.insert(1, "Prout (défaut)")
        liste2.insert(2, "Prout")
        liste2.insert(3, "Prout")
        liste2.insert(4, "Prout")

        self.play = Button(Midframe, text="Commencer à jouer",  font='Cambria 14', width="9", bg="#cde3f2", command = Interface_game)
        #Il faut que le paramètre sélectionné soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        # quand on débute le jeu, on ouvre l'interface de jeu
        # si tous les paramètres de la grille sont pas remplis, message d'erreur ou utilisation de paramètres par défaut ? 

        Bottomframe = Frame(self, fold = 2)
        self.scores = Button(Bottomframe, text='Esprit compétitif ? Consultez le tableau des scores',  font='Cambria 10', width="9", bg="#cde3f2", command = tableaudesscores)
        # tableau des scores dans un ficiher texte ou excel ? 
        self.regles = Button(Bottomframe, text='Besoin d\'aide ? Consultez les règles du jeu',  font='Cambria 10', width="9", bg="#cde3f2", command = fenetreregles)
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

        def create_drop() :
            pass


if __name__ == "__main__":
  # t = [(2,'r'),(4,'d'),(1,'k'),(2,'c')]
  # t.sort(reverse=True)
  # print(t)
  # g = grid(5,3,0)
  # for i in range(g.col): print(g[1,i])
  # # print(g)
  Interface_menu()
#Interface_game(6,5,3)

