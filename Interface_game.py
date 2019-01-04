from ezTK import *
from Interface_scores import *
from Interface_regles import *
from Drop import *
from time import sleep
# ------------------------------------------------------------------------------

class Interface_game(Win):
    """..."""
    def __init__(self,rows=8, cols=5, nbNewBricks=2, size=54, name = 'Anonyme'):
        Win.__init__(self, title='DROP', bg=('#116269'),op=10,key=self.event)
        self.master.resizable(False,False)
        rows += nbNewBricks+1
        self.end = False
        self.txtScore = '0'
        self.bg = '#116269'
        self.colors = ['#116269','#041725', '#C34223', '#F38D1F', '#FFED90', '#28FB57', '#00FFD2', '#428BFF', '#4007C4', '#000FFF', '#000000']
        self.score = Label(self, text=self.txtScore, font='Cambria 14', width="2", bg=self.colors[0])
        self.name = name
        #Paramètres de base de l'interface de jeu

        self.frameButtonsUp = Frame(self,op=10)

        self.reset = Button(self.frameButtonsUp, text='Reset', font='Cambria 11', width="5", height='1', command=self.resetGrid)
        #Recommencer une partie
        self.regles = Button(self.frameButtonsUp, text='Règles', font='Cambria 11', width="5", height='1', command=Regles)
        #Affiche les règles dans une nouvelle fenêtre
        self.ButtonScores = Button(self.frameButtonsUp, text='Scores', font='Cambria 11', width="5", height='1', command=self.scores)
        #Affiche les 10 meilleurs scores
        self.txtend = Label(self, text='Perdu', font='Cambria 20', width="15", fg=self.bg)
        #Echec du joueur

        self.frameGrid = Frame(self,fold=cols,op=3)
        for n in range(cols * rows): Brick(self.frameGrid, width=size, height=size, bd=0)
        #Création de la grille de jeu

        self.returnMenu = Button(self, text='Menu', font='Cambria 11', width="15", height='1', command=self.returnMenu)
        #Retour au menu
        self.drop = Drop(rows,cols,nbNewBricks,self.name)
        #Appel de la classe Drop - création de la partie, gère les mécanismes du jeu

        self.resetGrid()

        self.loop()

    def show(self):
        """Mise à jour de l'interface du jeu"""
        self.score['text'] = self.drop.score
        for r in range(self.drop.rows):
            for c in range(self.drop.cols):
                self.frameGrid[r][c]['bg'] = self.colors[self.drop.grid[r,c]]
        self.frameGrid.update()

    def resetGrid(self):
        """Reset la partie actuelle"""
        self.drop.reset()
        self.txtend['fg'] = self.bg
        self.end = False
        self.show()

    def returnMenu(self):
        self.exit()
        #Retour au menu

    def scores(self):
        """Affichage des scores"""
        interface = Interface_scores()

    def event(self, widget, code, mods):
        """Récupère les touches appuyées par l'utilisateur etlance la fonction correspondante (contrôle des bricks à poser)"""
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

    def stepBreak(self):
        """Lancement des fonctions permettant de tester si il y a besoin de break et d'effectuer les potentiels breaks"""
        self.drop.step()
        self.show()
        # Premier teste et peut-être break
        while self.drop.stopBreak == False:
            sleep(0.5)
            self.drop.step()
            self.show()
        # teste et peut-être break (avec des pauses) tant qu'il y a des possibilités
        if self.drop.endGame():
            self.txtend['fg'] = self.colors[1]
            self.end = True
        else:
            self.drop.newBricks()
        # Fin de la partie ? Sinon, création des nouvelles bricks à jouer
        self.show()
        self.drop.nbStep = 0
        self.drop.stopBreak = False
