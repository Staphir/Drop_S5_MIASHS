30/11/2018 :
- Création d'un diagramme de classe que l'on doit modifier car lors de l'implémentation on s'est rendu compte qu'il fallait scinder en deux la classe Interface
- Implémentation de la structure du programme presque finit

- 1ère version du début du jeu (à modifier pour avoir des échanges entre les classes) :
    -> création de la fenêtre et de la grille en fonction de la taille donnée et du nombre de nouvelles briques à chaque tour
    -> fonctions de déplacements, rotations et "descente" de briques
    -> affichage et mise à jour de la grille

14/12/2018 :
- Mise à jour du diagramme de classe
- Début de création du menu :
    -> interface simple
    -> non relié au reste du programme
- fonctions permettant de vérifier les cases à détruire, les détruires, remplacer par une case de valeur +1 et appliquer la gravité (step, lookBricks, breaks et gravity)
   '-> cette ensemble de fonctions ne foctionne pas toujours comme il faudrait (problème quand plusieurs suppressions doivent se faire en même temps ou à la suite)