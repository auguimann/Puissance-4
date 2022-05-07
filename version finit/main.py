from puissance4 import *
from colors import *

partie = Game()
colors = Colors()
partie.init_joueur()

print(partie.grille_init())

while not (partie.gagne(0) or partie.gagne(1)):
    partie.tour_joueur(partie.tour)
    print(partie.affiche_grille())

if partie.gagne(0):
    print((partie.players[0][
        'name'] + " a gagné !"))
else:
    print((partie.players[1]['name'] + " a gagné !" ))
