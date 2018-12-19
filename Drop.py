# ------------------------------------------------------------------------------
from ezTK import *
from Grid import *
import random
# ------------------------------------------------------------------------------

class Drop():

    def __init__(self, rows=6, cols=5, nbNewBricks=3):
        self.rows = rows
        self.cols = cols
        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.level = 2
        self.ligne = True
        self.score = '0'
        self.stopBreak = False
        self.listNewBricks = []

        #Création de la grille vide
        self.grid = grid(self.rows, self.cols, 0)

    def reset(self):
        self.level = 2
        for r in range(self.rows):
            for c in range(self.cols):
                if r < self.nbBricks + 1:
                    self.grid[r, c] = 0
                else:
                    self.grid[r, c] = 1
        self.newBricks()

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
        for debut in range(self.nbBricks-1,-1,-1):
            for x in range(debut,self.rows-1):
                for y in range(0,self.cols):
                    if self.grid[x,y] > 1 and self.grid[x+1,y] in (1,0):
                        self.grid[x+1,y] = self.grid[x,y]
                        if x <= self.nbBricks:
                            self.grid[x,y] = 0
                        else:
                            self.grid[x,y] = 1
        # N = self.nbBricks
        # debut = False
        # col = 0
        #
        # while debut == False:
        #     if self.grid[N-1,col] != 0:
        #         debut = True
        #         break
        #     col += 1
        #
        # if self.ligne == True:
        #     for i in range(col, col+self.nbBricks):
        #         j=self.nbBricks+1
        #         while j < self.rows:
        #             if self.grid[j,i] > 1:
        #                 self.grid[j-1,i] = self.grid[self.nbBricks-1,i]
        #                 self.grid[self.nbBricks-1,i] = 0
        #                 break
        #             else:
        #                 j += 1
        #         if j == self.rows:
        #             self.grid[j-1, i] = self.grid[self.nbBricks-1, i]
        #             self.grid[self.nbBricks-1, i] = 0
        # else:
        #     for i in reversed(range(self.nbBricks)):
        #         j=self.nbBricks+1
        #         while j < self.rows:
        #             if self.grid[j,col] > 1:
        #                 self.grid[j-1,col] = self.grid[i,col]
        #                 self.grid[i,col] = 0
        #                 break
        #             else:
        #                 j += 1
        #         if j == self.rows:
        #             self.grid[self.rows-1, col] = self.grid[i, col]
        #             self.grid[i, col] = 0

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
            if not cMax > self.nbBricks-2:
                for i in range(N):
                    self.grid[i,N-1] = self.grid[i,cMax]
                    self.grid[i,cMax] = 0
                cMax = N-1
            for i in reversed(range(N)):
                self.grid[N-1,cMax-i] = self.grid[i,cMax]
                self.grid[i,cMax] = 0
            self.ligne = True

    # ATENTION : 1) le plus bas --- 2) le plus à gauche
    def step(self):
        print("step")
        self.stopBreak = True
        self.listNewBricks = []
        for x in range(self.rows-1,0,-1):
            for y in range(0,self.cols):
                listBricks = []
                listBricks = self.lookBricks(listBricks,(x,y))
                if len(listBricks) > 2:
                    print(listBricks)
                    self.breaked(listBricks)
        self.addNewBricks()
        self.fall()

    def lookBricks(self, listBricks, coordonnees):
        x = coordonnees[0]
        y = coordonnees[1]
        around = [(x,y),(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
        if self.grid[x,y] > 1:
            for xy in around:
                if not (xy[0] < 0 or xy[1] < 0 or xy[0] >= self.rows or xy[1] >= self.cols):
                    if self.grid[xy[0],xy[1]] == self.grid[x,y] and xy not in listBricks:
                        listBricks.append(xy)
                        listBricks = self.lookBricks(listBricks, xy)
        return listBricks

    def breaked(self, listBricks):
        self.stopBreak = False
        newBrick = self.grid[listBricks[0]] + 1
        self.listNewBricks.append((listBricks[0][0],listBricks[0][1],newBrick))
        if newBrick > self.level:
                self.level += 1
        for i in range(0,len(listBricks)):
            if listBricks[i][0] <= self.nbBricks:
                self.grid[listBricks[i]] = 0
            else:
                self.grid[listBricks[i]] = 1

    def addNewBricks(self):
        for tuple in self.listNewBricks:
            self.grid[tuple[0],tuple[1]] = tuple[2]

    def endGame(self):
        c = 0
        for i in range(self.grid.col): c += self.grid[self.nbBricks,i]
        if c == 0:
            return False
        else:
            return True