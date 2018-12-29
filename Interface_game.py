from ezTK import *
from Interface_scores import *
from Drop import *
from time import sleep
# ------------------------------------------------------------------------------

class Interface_game(Win):

    def __init__(self,rows=6, cols=5, nbNewBricks=3, size=64, name = 'Unknow'):
        Win.__init__(self, title='DROP', bg=('#116269'),op=10,key=self.event)
        print(name)
        rows += nbNewBricks+1
        self.end = False
        self.txtScore = '0'
        self.bg = '#116269'
        self.colors = ['#116269','#041725', '#C34223', '#F38D1F', '#FFED90', '#28FB57', '#00FFD2', '#428BFF', '#4007C4', '#000FFF', '#000000']
        self.score = Label(self, text=self.txtScore, font='Cambria 14', width="2", bg=self.colors[0])
        self.name = name

        self.frameButtonsUp = Frame(self,op=10)

        self.reset = Button(self.frameButtonsUp, text='Reset', font='Cambria 11', width="5", height='1', command=self.resetGrid)
        self.regles = Button(self.frameButtonsUp, text='Règles', font='Cambria 11', width="5", height='1', command=self.rules)
        self.ButtonScores = Button(self.frameButtonsUp, text='Scores', font='Cambria 11', width="5", height='1', command=self.scores)
        self.txtend = Label(self, text='Perdu', font='Cambria 20', width="15", fg=self.bg)

        self.frameGrid = Frame(self,fold=cols,op=3)
        for n in range(cols * rows): Brick(self.frameGrid, width=size, height=size, bd=0)

        self.returnMenu = Button(self, text='Menu', font='Cambria 11', width="15", height='1', command=self.returnMenu)
        self.drop = Drop(rows,cols,nbNewBricks,self.name)

        self.resetGrid()

        self.loop()

    def show(self):
        self.score['text'] = self.drop.score
        for r in range(self.drop.rows):
            for c in range(self.drop.cols):
                self.frameGrid[r][c]['bg'] = self.colors[self.drop.grid[r,c]]
        self.frameGrid.update()

    def resetGrid(self):
        self.drop.reset()
        self.txtend['fg'] = self.bg
        self.end = False
        self.show()

    def returnMenu(self):
        pass

    def rules(self):
        pass

    def scores(self):
        interface = Interface_scores()

    def event(self, widget, code, mods):
        if self.end == False:
            if code == 'Down':
                self.drop.fall()
                self.show()
                self.after(500, self.stepBreak)
            if code == 'Left':
                self.drop.moveLeft()
                self.show()
            if code == 'Right':
                self.drop.moveRight()
                self.show()
            if code == 'Up':
                self.drop.rotate()
                self.show()
        #si on actionne la touche bas, gauche, droite ou haut, on renvoie la fonction correspondante

    def stepBreak(self):
        self.drop.step()
        self.show()
        while self.drop.stopBreak == False:
            sleep(0.5)
            self.drop.step()
            self.show()
        if self.drop.endGame():
            self.txtend['fg'] = self.colors[1]
            self.end = True
        else:
            self.drop.newBricks()
        self.show()
        self.drop.nbStep = 0
        self.drop.stopBreak = False
    #!!! Dialogue entre interface et Drop pendant l'ensemble du break (surtout si plusieurs break) !!!