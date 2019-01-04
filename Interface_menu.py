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
        # trouver comment donner une taille fixe à la fenêtre 

        self.nbBricks = nbNewBricks
        self.varSize = size
        self.rows = rows
        self.cols = cols
        self.name = StringVar(self,'Anonyme')

        Topframe = Frame(self, fold = 1)
        Label(Topframe, text="BIENVENUE SUR LE DROP", font='Cambria 30', bg="#cde3f2", relief ="groove")

        Midframe = Frame(self, fold = 2)
        Label(Midframe, text="Tout d'abord, entrez votre nom de joueur \n", font='Cambria 13', width="50", bg="#cde3f2", relief ="groove")
        self.nameEntry = Entry(Midframe,textvariable=self.name, font='Cambria 13', width="29", bg="#cde3f2")
        #Il faut que le nom soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        #message d'erreur si il n'y a pas de pseudo

        self.gridSize = Label(Midframe, text="Sélectionnez le format de grille avec lequel vous souhaitez jouer \n", font='Cambria 13', width="50", bg="#cde3f2")
        self.liste = Listbox(Midframe,selectmode='SINGLE',width='30')
        self.liste.insert(1, "8 lignes, 5 colonnes (défaut)")
        self.liste.insert(2, "16 lignes, 10 colonnes (maxi)")
        self.liste.insert(3, "8 lignes, 8 colonnes (carré)")
        self.liste.insert(4, "6 lignes, 4 colonnes (mini)")
        #Il faut que le paramètre sélectionné soit enregistré quand on lance le jeu (et aussi sur les scores ?)

        self.newBricks = Label(Midframe, text="Combien de briques voulez-vous gérer par tour ?",  font='Cambria 13', width="50", bg="#cde3f2" )
        self.spin = IntVar(self,2)
        self.nbBricksSpin = Spinbox(Midframe, textvariable=self.spin, from_=2,to=4,state='readonly',width='31',bg='#cde3f2')

        self.play = Button(Midframe, text="Commencer à jouer",  font='Cambria 13', width="9", bg="#cde3f2", command = self.create_drop)
        #Il faut que le paramètre sélectionné soit enregistré quand on lance le jeu (et aussi sur les scores ?)
        # quand on débute le jeu, on ouvre l'interface de jeu
        # si tous les paramètres de la grille sont pas remplis, message d'erreur ou utilisation de paramètres par défaut ? 

        Bottomframe = Frame(self, fold = 2)
        self.scores = Button(Bottomframe, text='Esprit compétitif ? Consultez le tableau des scores',  font='Cambria 10', width="35", bg="#cde3f2", command = Interface_scores)
        # tableau des scores dans un fichier texte ou excel ? -> texte (save.txt)
        self.regles = Button(Bottomframe, text='Besoin d\'aide ? Consultez les règles du jeu',  font='Cambria 10', width="35", bg="#cde3f2", command = Regles)
        # ouvre une fenetre ou les regles s'affichent tout simplement
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

    def create_drop(self):
        """Création d'une fenêtre de jeu avec les paramètres séléctionnées"""
        self.nbBricks = self.spin.get()
        if self.liste.curselection():
            self.rows_and_cols_selected()
        self.name = self.nameEntry.get()
        if self.name == '' or not self.name.isalnum():
            self.name = 'Unknow'
        Interface_game(self.rows,self.cols,self.nbBricks,self.varSize,self.name)