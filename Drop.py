# ------------------------------------------------------------------------------
from ezTK import *
from Grid import *
import random
# ------------------------------------------------------------------------------

class Drop():

    def __init__(self, rows=6, cols=5, nbNewBricks=3, name='Unknow'):
        self.rows = rows
        self.cols = cols
        self.nbBricks = nbNewBricks
        rows += self.nbBricks + 1
        self.level = 2
        self.ligne = True
        self.score = '0'
        self.stopBreak = False
        self.listNewBricks = []
        self.nbStep = 0
        self.name = name

        #Création de la grille vide
        self.grid = grid(self.rows, self.cols, 0)

    def reset(self):
        self.level = 2
        self.score = '0'
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
        self.nbStep += 1
        self.stopBreak = True
        self.listNewBricks = []
        for x in range(self.rows-1,0,-1):
            for y in range(0,self.cols):
                listBricks = []
                listBricks = self.lookBricks(listBricks,(x,y))
                if len(listBricks) > 2:
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
        self.score = str(int(self.score)+(((self.grid[listBricks[0]]-1)*10)*len(listBricks))*self.nbStep)
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
            self.saveScore()
            return True

    def saveScore(self):
        name_file = "save.txt"
        new_file = ""
        list_scores = []
        # Lecture scores
        try:
            r = open(name_file, "r")
        except IOError:
            print(name_file, ": fichier inconnu")
            return
        try:
            list_scores.append((self.score,self.name))
            for line in r:
                table = line.split(";")
                list_scores.append((table[1],table[0]))
            sorted(list_scores,reverse=True)
            r.close()
        except ValueError:
            print("échec import txt")
        # Ecriture scores
        try:
            w = open(name_file, "w")
        except IOError:
            print(name_file, ": fichier inconnu")
            return
        try:
            for i in range(0,len(list_scores)-1):
                new_file += list_scores[i][1] + ';' + list_scores[i][0] + ';' + '\n'
            new_file += list_scores[len(list_scores)-1][1] + ';' + list_scores[len(list_scores)-1][0]
            w.write(new_file)
            w.close()
        except ValueError:
            print("échec écriture txt")