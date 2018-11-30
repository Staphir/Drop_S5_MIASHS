from ezTK import *
from Drop import *


# ------------------------------------------------------------------------------

# fonction de création de la grille de Drop par-dessus l'interface menu

class Interface_menu(Win):

    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=3):
        Win.__init__(self, title='DROP', bg=('#0066CC'), op=10)

        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.rows = rows
        self.cols = cols

        Topframe = Frame(self, fold=1)
        Label(Topframe, text="Bienvenue sur le Drop ! ", font='Cambria 30', bg="#0066CC")

        Midframe = Frame(self, fold=2)
        self.name = Label(Midframe, text="Entrez votre nom de joueur", font='Cambria 14', width="9", bg="#0066CC")
        self.gridSize = Label(Midframe, text="Sélectionnez le format de grille avec lequel vous souhaitez jouer",
                              font='Cambria 14', width="9", bg="#0066CC")
        self.newBricks = Label(Midframe, text="Combien de briques voulez-vous gérer par tour ?", font='Cambria 14',
                               width="9", bg="#0066CC")
        self.play = Button(Midframe, text="Commencer à jouer", font='Cambria 14', width="9", bg="#CDCDCD")

        Bottomframe = Frame(self, fold=2)
        self.scores = Button(Bottomframe, text='Esprit compétitif ? Consultez le tableau des scores', font='Cambria 10',
                             width="9", bg="#CDCDCD")
        self.regles = Button(Bottomframe, text='Besoin d\'aide ? Consultez les règles du jeu', font='Cambria 10',
                             width="9", bg="#CDCDCD")

        self.loop()

        # def play(self):

        #     self.reset = Button(frame, text='RESET', width="9", bg="#CDCDCD", command= drop.reset)
        #     frameGrid
        #     self.brickcolor = ['#bf3f28', '#f19908', ' #feedce', '#85ec62', ' #62ecea ', ' #358ecb ', ' #2e429e ', ' #eb6ff3 ', ' #fc2737 ', '#000000']

        def create_drop():
            pass


