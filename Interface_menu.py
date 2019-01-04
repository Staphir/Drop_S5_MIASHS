from ezTK import *
from Drop import *
from Interface_game import *
from Interface_scores import *
from Interface_regles import *
# from tkinter import *
# ------------------------------------------------------------------------------

class Interface_menu(Win):
    """..."""
    def __init__(self, rows=8, cols=5, size=64, nbNewBricks=2):

        Win.__init__(self, title='DROP', bg=('#cde3f2'),op=10)
        self.nbBricks = nbNewBricks
        self.varSize = size
        self.rows = rows
        self.cols = cols
        self.name = StringVar(self,'Anonyme')

        Topframe = Frame(self, fold = 1)
        Label(Topframe, text="BIENVENUE SUR LE DROP", font='Cambria 30', bg="#cde3f2", relief ="groove")
        #Titre du menu

        Midframe = Frame(self, fold = 2)
        Label(Midframe, text="Tout d'abord, entrez votre nom de joueur \n", font='Cambria 13', width="50", bg="#cde3f2", relief ="groove")
        self.nameEntry = Entry(Midframe,textvariable=self.name, font='Cambria 13', width="29", bg="#cde3f2")
        #Saisie du nom de l'utilisateur 

        self.gridSize = Label(Midframe, text="Sélectionnez le format de grille avec lequel vous souhaitez jouer \n", font='Cambria 13', width="50", bg="#cde3f2")
        self.liste = Listbox(Midframe,selectmode='SINGLE',width='30')
        self.liste.insert(1, "8 lignes, 5 colonnes (défaut)")
        self.liste.insert(2, "16 lignes, 10 colonnes (maxi)")
        self.liste.insert(3, "8 lignes, 8 colonnes (carré)")
        self.liste.insert(4, "6 lignes, 4 colonnes (mini)")
        #Choix de la taille de la grille

        self.newBricks = Label(Midframe, text="Combien de briques voulez-vous gérer par tour ?",  font='Cambria 13', width="50", bg="#cde3f2" )
        self.spin = IntVar(self,2)
        self.nbBricksSpin = Spinbox(Midframe, textvariable=self.spin, from_=2,to=4,state='readonly',width='31',bg='#cde3f2')
        #Choix du nombre de briques à faire tomber 
        
        self.play = Button(Midframe, text="Commencer à jouer",  font='Cambria 13', width="9", bg="#cde3f2", command = self.create_drop)
        #Lancer le jeu

        Bottomframe = Frame(self, fold = 2)
        self.scores = Button(Bottomframe, text='Esprit compétitif ? Consultez le tableau des scores',  font='Cambria 10', width="35", bg="#cde3f2", command = Interface_scores)
        #Ouvre le tableau des scores
        self.regles = Button(Bottomframe, text='Besoin d\'aide ? Consultez les règles du jeu',  font='Cambria 10', width="35", bg="#cde3f2", command = Regles)
        #Affiche les règles dans une nouvele fenêtre
        self.loop()

    def rows_and_cols_selected(self):
        if self.liste.curselection()[0] == 0:
            self.rows, self.cols = 8,5
        if self.liste.curselection()[0] == 1:
            self.rows, self.cols = 16,10
        if self.liste.curselection()[0] == 2:
            self.rows, self.cols = 8,8
        if self.liste.curselection()[0] == 3:
            self.rows, self.cols = 6,4
        #Paramétrage de la taille du Drop en fonction du choix du joueur

    def create_drop(self):
        """Création d'une fenêtre de jeu avec les paramètres séléctionnées"""
        self.nbBricks = self.spin.get()
        if self.liste.curselection():
            self.rows_and_cols_selected()
        self.name = self.nameEntry.get()
        nameSplited = self.name.split(' ')
        self.name = ''
        for s in nameSplited:
            if s == '' or not s.isalnum():
                nameSplited = 'Anonyme'
                break
            else:
                self.name += s + ' '
        Interface_game(self.rows,self.cols,self.nbBricks,self.varSize,self.name)
