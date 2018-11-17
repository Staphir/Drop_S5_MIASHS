# ------------------------------------------------------------------------------
from ezTK import *
from Grid import *
import random
# ------------------------------------------------------------------------------

class Drop(Win):

    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=3):
        Win.__init__(self, title='DROP', bg=('#0066CC'),op=10, key=self.event)
        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.rows = rows
        self.cols = cols
        self.colors = ['#0066CC','#CDCDCD', '#FF0000', '#00FF00', '#0000FF']
        self.level = 3
        self.ligne = True

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

    def event(self, widget, code, mods):
        if code == 'Down':
            self.moveDown()
            self.show()
        if code == 'Left':
            self.moveLeft()
            self.show()
        if code == 'Right':
            self.moveRight()
            self.show()
        if code == 'Up':
            self.rotate()
            self.show()
        #si on actionne la touche bas, gauche, droite ou haut, on renvoie la fonction correspondante

    def show(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.frameGrid[r][c]['bg'] = self.colors[self.grid[r,c]]

    def reset(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if r<self.nbBricks + 1:
                    self.grid[r,c] = 0
                else:
                    self.grid[r,c] = 1
        self.newBricks()
        self.show()

    def newBricks(self):
        for c in range(self.nbBricks):
            self.grid[self.nbBricks-1,c] = random.randint(2,self.level)
        self.ligne = True

    def moveLeft(self):
        if self.grid[self.nbBricks-1,0] == 0:
            for i in range(self.nbBricks):
                for j in range(1,self.cols):
                    self.grid[i,j-1] = self.grid[i,j]
                    self.grid[i, j] = 0

    def moveRight(self):
        if self.grid[self.nbBricks-1,self.cols-1] == 0:
            for i in range(self.nbBricks):
                for j in reversed(range(1,self.cols)):
                    self.grid[i,j] = self.grid[i,j-1]
                    self.grid[i,j-1] = 0

    def moveDown(self):
        N = self.nbBricks
        debut = False
        col = 0

        while debut == False:
            if self.grid[N-1,col] != 0:
                debut = True
                break
            col += 1

        if self.ligne == True:
            for i in range(col, col+self.nbBricks):
                j=self.nbBricks+2
                while j < self.rows:
                    if self.grid[j,i] > 1:
                        self.grid[j-1,i] = self.grid[self.nbBricks-1,i]
                        self.grid[self.nbBricks-1,i] = 0
                        print(self.grid[j-1,i])
                        break
                    else:
                        j += 1
                if j == self.rows:
                    self.grid[j-1, i] = self.grid[self.nbBricks-1, i]
                    self.grid[self.nbBricks-1, i] = 0
        else:
            for i in reversed(range(self.nbBricks)):
                j=self.nbBricks+2
                while j < self.rows:
                    if self.grid[j,col] > 1:
                        self.grid[j-1,col] = self.grid[i,col]
                        self.grid[i,col] = 0
                        break
                    else:
                        j += 1
                if j == self.rows:
                    self.grid[self.rows-1, col] = self.grid[i, col]
                    self.grid[i, col] = 0
        self.newBricks()

    def rotate(self):
        N = self.nbBricks
        debut = False
        cMax = 0

        while debut == False:
            if self.grid[N-1,cMax] != 0:
                debut = True
                break
            cMax += 1

        if self.ligne == True:
            cMax = cMax + self.nbBricks-1

        if self.ligne == True:
            for i in range(N-1):
                self.grid[i,cMax] = self.grid[N-1,cMax-N+1+i]
                self.grid[N-1,cMax-N+1+i] = 0
            self.ligne = False
        else:
            if cMax > self.nbBricks-2:
                for i in reversed(range(N)):
                    self.grid[N-1,cMax-i] = self.grid[i,cMax]
                    self.grid[i,cMax] = 0
                self.ligne = True

    def dfs(self, noeud, other):
        pass
    # ATENTION : 1) le plus bas --- 2) le plus à gauche

    def breaked(self, listSquares):
        for i in listSquares:
            self.grid[i] = 1