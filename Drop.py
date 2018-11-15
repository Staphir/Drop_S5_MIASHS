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

        self.begin = 1
        self.end = 2

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
        positionAccepted = False
        if self.grid[self.nbBricks-1,0] == 0:
            positionAccepted = True

        # if positionAccepted == True:
            # lNewMax = self.nbBricks-1
            # newColors = [[self.gridBricks[lNewMax][i + self.begin]['bg']] for i in range(self.end - self.begin + 1)]
            # for i in range(self.end-self.begin+1):
            #     self.gridBricks[lNewMax][self.begin-1+i]['bg'] = newColors[i]
            # self.gridBricks[lNewMax][self.end]['bg'] = self.colors[0]
            # self.begin, self.end = self.begin-1, self.end-1

    def moveRight(self):
        positionAccepted = False
        if self.grid[self.nbBricks-1,self.cols-1] == 0:
            positionAccepted = True

        # if positionAccepted == True:
            # lNewMax = self.nbBricks-1
            # newColors = [[self.gridBricks[lNewMax][i + self.begin]['bg']] for i in range(self.end - self.begin + 1)]
            # for i in range(self.end-self.begin+1):
            #     self.gridBricks[lNewMax][self.end+1-i]['bg'] = newColors[self.end-self.begin-i]
            # self.gridBricks[lNewMax][self.begin]['bg'] = self.colors[0]
            # self.begin, self.end = self.begin+1, self.end+1

    def moveDown(self):
        colorBase = [self.colors[0], self.colors[1]]
        newColors = [self.colors[2], self.colors[3]]
        for i in range (3):
            self.gridBricks[i][self.begin]['bg'] = self.colors[0]
            self.gridBricks[i + 1][self.begin]['bg'] = newColors[0]

        for j in range (3):
            self.gridBricks[j][self.end]['bg'] = self.colors[0]
            self.gridBricks[j + 1][self.end]['bg'] = newColors[0]

        i=3
        j=3
        while i < self.rows:
            if not self.gridBricks[i+1][self.begin]['bg'] in colorBase:
                break
            else:
                self.gridBricks[i][self.begin]['bg'] = self.colors[1]
                self.gridBricks[i+1][self.begin]['bg'] = newColors[0]
            if i+2 >= self.rows:
                break
            else:
                i = i + 1

        while j < self.rows:
            if not self.gridBricks[j+1][self.end]['bg'] in colorBase:
                break
            else:
                self.gridBricks[j][self.end]['bg'] = self.colors[1]
                self.gridBricks[j+1][self.end]['bg'] = newColors[1]
            if j+2 >= self.rows:
                break
            else:
                j = j + 1

    def rotate(self):
        N = self.nbBricks
        debut = False
        cMax = N-1
        while debut == False and self.grid[N-1,cMax] != 0:
            if self.grid[N-1,cMax] != 0:
                debut = True
            cMax += 1
        cMax = cMax-1
        if self.ligne == True:
            for i in range(N-1):
                self.grid[i,cMax] = self.grid[N-1,cMax-N+1+i]
                self.grid[N-1,cMax-N+1+i] = 0
            self.ligne = False
        else:
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