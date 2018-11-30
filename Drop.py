# ------------------------------------------------------------------------------
from ezTK import *
from Grid import *
import random
# ------------------------------------------------------------------------------

class Drop():

    def __init__(self, rows=8, cols=5, nbNewBricks=3):
        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.rows = rows
        self.cols = cols
        self.level = 3
        self.ligne = True
        self.score = '0'

        #Création de la grille vide
        self.grid = grid(self.rows, self.cols, 0)

    def event(self, widget, code, mods):
        if code == 'Down':
            self.fall()
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
        #modification score
        #possibilité d'ajout de nouvelle couleur
        #refresh
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

    def fall(self):
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

    # ATENTION : 1) le plus bas --- 2) le plus à gauche

    def breaked(self, listSquares):
        for i in listSquares:
            self.grid[i] = 1