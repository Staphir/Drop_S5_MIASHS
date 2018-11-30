from ezTK import *
from Drop import *
# ------------------------------------------------------------------------------

class Interface_game(Win):

    def __init__(self,rows=8, cols=5, size=64, nbNewBricks=3):
        Win.__init__(self, title='DROP', bg=('#0066CC'),op=10)
        self.score = '0'
        self.colors = ['#0066CC','#CDCDCD', '#FF0000', '#00FF00', '#0000FF']
        self.returnMenu = Button(self, text='Menu', font='Cambria 11', width="15", height='1', bg=self.colors[1], command=self.returnMenu)
        self.drop = Drop()

        self.frameGrid = Frame(self,fold=cols,op=3)
        for n in range(cols * rows): Brick(self.frameGrid, width=size, height=size, bd=0)

        self.resetGrid()
        #dans le tableau, si on est avant la ligne 4, alors la grille a la couleur du fond
        #sinon la grille a la couleur de la zone jouable

        #grille [x][-y] debut en haut a gauche
        self.gridBricks = self[0]
        # self.gridBricks[self.nbBricks-1][1]['bg'] = self.colors[2]
        #deuxieme ligne deuxieme colonne : initiatisation d'une brique colorée a empiler
        # self.gridBricks[self.nbBricks-1][2]['bg'] = self.colors[3]
        # deuxieme ligne troisieme colonne : initiatisation d'une brique colorée a empiler

        self.loop()

    def show(self):
        pass

    def resetGrid(self):
        pass

    def returnMenu(self):
        pass

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

    #!!! Dialogue entre interface et Drop pendant l'ensemble du break (surtout si plusieurs break) !!!