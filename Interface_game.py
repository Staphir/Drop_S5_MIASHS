from ezTK import *
from Drop import *
# ------------------------------------------------------------------------------

class Interface_game(Win):

    def __init__(self,rows=6, cols=5, size=64, nbNewBricks=3, maxLevel=5):
        Win.__init__(self, title='DROP', bg=('#0066CC'),op=10,key=self.event)
        rows += nbNewBricks
        self.txtScore = '0'
        self.colors = ['#0066CC','#CDCDCD', '#FF0000', '#00FF00', '#0000FF', '#FFFFFF']
        self.score = Label(self, text=self.txtScore, font='Cambria 14', width="2", bg="#0066CC")

        self.reset = Button(self, text='Reset', font='Cambria 11', width="15", height='1', bg=self.colors[1], command=self.resetGrid)
        self.regles = Button(self, text='Règles', font='Cambria 11', width="15", height='1', bg=self.colors[1], command=self.rules)

        self.frameGrid = Frame(self,fold=cols,op=3)
        for n in range(cols * rows): Brick(self.frameGrid, width=size, height=size, bd=0)

        self.returnMenu = Button(self, text='Menu', font='Cambria 11', width="15", height='1', bg=self.colors[1], command=self.returnMenu)
        self.drop = Drop(rows,cols)

        self.resetGrid()

        self.loop()

    def show(self):
        for r in range(self.drop.rows):
            for c in range(self.drop.cols):
                self.frameGrid[r][c]['bg'] = self.colors[self.drop.grid[r,c]]

    def resetGrid(self):
        self.drop.reset()
        self.show()

    def returnMenu(self):
        pass

    def rules(self):
        pass

    def event(self, widget, code, mods):
        if code == 'Down':
            self.drop.fall()
            self.show()
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
        while self.drop.stopBreak == False:
            self.drop.step()
            self.show()
    #!!! Dialogue entre interface et Drop pendant l'ensemble du break (surtout si plusieurs break) !!!