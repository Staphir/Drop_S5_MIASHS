# ------------------------------------------------------------------------------
from ezTK import *
# ------------------------------------------------------------------------------

class Grid(Win):

    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=4):
        Win.__init__(self, title='DROP', bg=('#0066CC'),op=10, key=self.event)
        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.rows = rows
        self.cols = cols
        self.colors = ['#0066CC','#CDCDCD', '#FF0000', '#00FF00', '#0000FF']

        self.grid = [[[] for i in range(cols)] for j in range(rows)]
        #Création de la grille vide
        frameGrid = Frame(self,fold=cols,op=3)

        for r in range(rows):
            for c in range(cols):
                if r<self.nbBricks + 1:
                    self.grid[r][c].append(Brick(frameGrid, height=size, width=size, bg=(self.colors[0]),bd=0))
                else:
                    self.grid[r][c].append(Brick(frameGrid, height=size, width=size, bg=(self.colors[1]),bd=0))
        #dans le tableau, si on est avant la ligne 4, alors la grille a la couleur du fond
        #sinon la grille a la couleur de la zone jouable

        self.begin = 1
        self.end = 2

        #grille [x][-y] debut en haut a gauche
        self.gridBricks = self[0]
        self.gridBricks[self.nbBricks-1][1]['bg'] = self.colors[2]
        #deuxieme ligne deuxieme colonne : initiatisation d'une brique colorée a empiler
        self.gridBricks[self.nbBricks-1][2]['bg'] = self.colors[3]
        # deuxieme ligne troisieme colonne : initiatisation d'une brique colorée a empiler
        self.loop()

    def event(self, widget, code, mods):
        if code == 'Down':
            self.moveDown()
        if code == 'Left':
            self.moveLeft()
        if code == 'Right':
            self.moveRight()
        if code == 'Up':
            self.rotate()
        #si on actionne la touche bas, gauche, droite ou haut, on renvoie la fonction correspondante

    # def rotate(self):


    def moveLeft(self):
        if self.begin-1 >= 0:
            lNewMax = self.nbBricks-1
            newColors = [[self.gridBricks[lNewMax][i + self.begin]['bg']] for i in range(self.end - self.begin + 1)]
            for i in range(self.end-self.begin+1):
                self.gridBricks[lNewMax][self.begin-1+i]['bg'] = newColors[i]
            self.gridBricks[lNewMax][self.end]['bg'] = self.colors[0]
            self.begin, self.end = self.begin-1, self.end-1

    def moveRight(self):
        if self.end+1 < self.cols:
            lNewMax = self.nbBricks-1
            newColors = [[self.gridBricks[lNewMax][i + self.begin]['bg']] for i in range(self.end - self.begin + 1)]
            for i in range(self.end-self.begin+1):
                self.gridBricks[lNewMax][self.end+1-i]['bg'] = newColors[self.end-self.begin-i]
            self.gridBricks[lNewMax][self.begin]['bg'] = self.colors[0]
            self.begin, self.end = self.begin+1, self.end+1

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


    def dfs(self, noeud, other):
        pass

    def breaked(self, listSquares):
        pass