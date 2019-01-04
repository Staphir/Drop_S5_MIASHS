from ezTK import *
# ------------------------------------------------------------------------------

class Regles(Win):
    """Création de la fenêtre affichant les règles"""

    def __init__(self):
        Win.__init__(self,bg=('#cde3f2'))
        regles = "Le but du jeu est de former des assemblages d'au moins 3 blocs \n adjacents de la même couleur. Chaque fois qu'un tel assemblage \n"\
        "est obtenu, il est remplacé par un bloc de plus haut niveau, \n caractérisé par une nouvelle couleur. \n"\
        "\n"\
        "Pour arriver à cela, vous devez réfléchir à la façon dont vous \n disposez les blocs dans la grille de jeu. Vous pouvez les \n"\
        "faire pivoter ou les décaler sur toute la largeur de la grille. \n"\
        "\n"\
        "Votre score est calculé en fonction de la taille des assemblages \n et de la couleur des blocs assemblés. Alors ne lésinez pas \n"\
        "sur la quantité... Mais n'oubliez pas que les blocs de haut \n"\
        "niveau sont plus longs à obtenir ! "
        self.txtend = Label(self, text=regles, font='Cambria 20', fg='#000000')
