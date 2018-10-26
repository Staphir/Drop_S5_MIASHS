# ==============================================================================
"""Project L3 : Drop"""
# ==============================================================================
__author__  = "Lucie Thomasson & Maxime Dulieu"
__version__ = "3.0" # toggle between two different master windows
__date__    = "2018-10-19"
# ==============================================================================
from GridClass import *
# ------------------------------------------------------------------------------

# ==============================================================================
if __name__ == "__main__": # testcode for class 'DemoWin'
  Grid()
# ==============================================================================

#pour déplacer les duos de carrés (et pivoter aussi) on parcourt chaque ligne de la
#zone non jouable et on sélectionne les cases qui ont une couleur différente de celle
#du fond

#agrandir la taille de la fenetre en fonction du nombre de carrés a placer (si on les met
#en vertical, augmenter le nombre de lignes de la zone non jouable)

#faire un test pour que le nombre de carres de depart ne depasse ni la largeur ni la
#hauteur de la grille jouable. Si les joueurs mettent trop grand en largeur, on remplace
#par la plus grande largeur de la grille jouable

#faire tourner les carrés a placer si on appuie sur la fleche du haut


#faire la fonction pour simuler les combos de carrés
# -> parcourir toute la grille a chaque tour
# -> combos de trois carrés ou plus
# -> il faut que les trois carrés ou plus se touchent à une extrémité
#     pas besoin qu'ils se touchent tous
# -> destruction de n-1 carrés, sauf celui le plus en bas a gauche
# -> celui restant prend la couleur au dessus
# -> les carres au-dessus des zones vides prennent la place de celles ci
#     décalage de tous les carrés au dessus du vide vers le bas
# -> on parcourt toute la grille a nouveau
# -> si on trouve des trios de carrés connectés ou plus, on réitère l'opération
# -> on réitère l'opération de décalage et de recherche jusqu'a ce qu'il
#    n'y ait plus aucun triplet ou plus

#intégrer toutes les couleurs de carrés

#intégrer les règles concernant les carrés
# -> rouge -> orange -> beige -> vert -> bleu ciel -> bleu moyen -> bleu foncé -> rose -> rouge -> noir -> la grille explose

#points par rapport aux carrés
# rouge : 10 points        bleu moyen : 60 points
# orange : 20 points       bleu fonce : 70 points
# beige : 30 points        rose : 80 points
# vert : 40 points         rouge: 90 points
# bleu ciel : 50 points    noir : 100 points

#faire un affichage du score additionnant les points
#on a des points rapportés à chaque fois que des carres explosent
#total des points gagnes = valeur de l'explosion d'un carre de couleur * nb carres de cette couleur exploses

#enregistrement total des points a la fin de la partie
#sauvegarde sur fichier en fonction de chaque taille de grille et de chaque taille de carres proposee
#sauvegarde dans l'ordre decroissant (high score)

#menu
#bouton recommencer partie
#menu déroulant avec taille grille
#menu déroulant avec taille groupes de carrés
#bouton pour commencer avec ces paramètres
#affichage des high scores en fonction ces paramètres dit plus haut
