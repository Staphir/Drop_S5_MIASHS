from ezTK import *
from Drop import *
# ------------------------------------------------------------------------------

class Interface(Win):

    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=3):
        Win.__init__(self, title='DROP', bg=('#0066CC'),op=10, key=self.event)
        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.rows = rows
        self.cols = cols
        self.colors = ['#0066CC','#CDCDCD', '#FF0000', '#00FF00', '#0000FF']

        frame= Frame(self)
        Button(frame, text='Reset', width="9", bg="#CDCDCD", command=self.reset)

        #Création de la grille vide
        self.grid = grid(self.rows, self.cols, 0)

        self.frameGrid = Frame(self,fold=cols,op=3)
        for n in range(cols * rows): Brick(self.frameGrid, width=size, height=size, bd=0)

        self.reset()
        #dans le tableau, si on est avant la ligne 4, alors la grille a la couleur du fond
        #sinon la grille a la couleur de la zone jouable

        #grille [x][-y] debut en haut a gauche
        self.gridBricks = self[0]
        # self.gridBricks[self.nbBricks-1][1]['bg'] = self.colors[2]
        #deuxieme ligne deuxieme colonne : initiatisation d'une brique colorée a empiler
        # self.gridBricks[self.nbBricks-1][2]['bg'] = self.colors[3]
        # deuxieme ligne troisieme colonne : initiatisation d'une brique colorée a empiler
        self.loop()
