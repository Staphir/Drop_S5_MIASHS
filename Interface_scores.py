from ezTK import *

class Interface_scores(Win):
    """..."""
    def __init__(self):
        Win.__init__(self, title='SCORES', bg=('#0066CC'), op='15')
        self.txtend = Label(self, text='Scores :', font='Cambria 20', fg='#000000')
        self.name_file = "save.txt"
        self.txtScores = self.uploadScore()
        self.scores = Label(self, text=self.txtScores, font='Cambria 20', fg='#000000')
        #Affichage des meilleurs scores des utilisateurs dans une fenêtre à part 

    def uploadScore(self):
        """Renvoie un string comportant les scores du fichier self.name_file (ici save.txt)
        IMPORTANT : séparateur ;"""
        txt = ''
        try:
            file = open(self.name_file, "r")
        except IOError:
            print(self.name_file, ": fichier inconnu")
            return
        try:
            for line in file:
                table = line.split(";")  # Création d’un tableau de chaque éléments
                txt += table[0] + ' : ' + table[1] + '\n'
            file.close()
        except ValueError:
            print("échec import txt")
        return txt
