from colors import *
class Game:
    def __init__(self):
        self.tab = []
        self.tour = 0
        self.joueur = []
        self.colors = Colors()

    def print_grille(self):
        grille = ''
        for lig in range(0, 6):
            grille += "\n|---|---|---|---|---|---|---|\n"
            for col in range(0, 7):
                player = self.check_cellule(col, lig)
                if not player:
                    player = ' '
                else:
                    player = self.joueur[0 if player['player'] == 'X' else 1]['color'] + player[
                        'player'] + self.colors.reset
                grille += "| %s " % player
            grille += '|'
        grille += '\n|---|---|---|---|---|---|---|'
        grille += '\n  1   2   3   4   5   6   7\n\n'
        return grille;

    def grille_init(self):
        self.tab = []
        grille = self.print_grille()
        return grille;

    def colonne_libre(self, colonne):
        return not self.check_cellule(colonne, 0)

    def check_cellule(self, colonne, ligne):
        tab = self.tab
        for i in range(0, len(tab)):
            if tab[i]['y'] == ligne and tab[i]['x'] == colonne:
                return self.tab[i]
        return False

    def place_jeton(self, colonne, joueur):
        signe = self.joueur[joueur]['signe']
        for i in range(6):
            if not (self.check_cellule(colonne, 5 - i)):
                self.tab.append({
                    'x': colonne,
                    'y': 5 - i,
                    'player': signe
                })
                return self

    def init_joueur(self):
        joueur1 = input("Quel est le nom du premier joueur ? ")
        joueur2 = input("Quel est le nom du second joueur ? ")
        self.joueur.extend([{
            'name': joueur1,
            'signe': 'x',
            'color': self.colors.jaune
        }, {
            'name': joueur2,
            'signe': 'o',
            'color': self.colors.cyan
        }])
        return self

    def check_verticale(self, joueur):
        celSuccessive = 0
        for col in range(0, 7):
            for lig in range(0, 6):
                cellule = self.check_cellule(col, lig)
                if cellule and cellule['player'] == self.joueur[joueur]['signe']:
                    celSuccessive += 1
                else:
                    celSuccessive = 0
                if celSuccessive > 3:
                    return True
        return False

    def check_horizontale(self, joueur):
        celSuccessive = 0
        for lig in range(0, 6):
            for col in range(0, 7):
                cellule = self.check_cellule(col, lig)
                if cellule and cellule['player'] == self.joueur[joueur]['signe']:
                    celSuccessive += 1
                else:
                    celSuccessive = 0
                if celSuccessive > 3:
                    return True
        return False

    def diagonale(self, joueur):
        for lig in range(6):
            for col in range(7):
                cellule = self.check_cellule(col, lig)
                if cellule and cellule['player'] == self.joueur[joueur]['signe']:
                    alignee = 1
                    for i in range(4):
                        cellule_decalee = False
                        if col > 2 and lig > 2:
                            cellule_decalee = self.check_cellule(col - i - 1, lig - i - 1)
                        elif col < 4 and lig > 2:
                            cellule_decalee = self.check_cellule(col + i + 1, lig - i - 1)
                        if cellule_decalee and cellule_decalee['player'] == self.joueur[joueur]['signe']:
                            alignee += 1
                        else:
                            break;
                        if alignee > 3:
                            return True
        return False

    def gagne(self, joueur):
        return self.check_horizontale(joueur) or self.check_verticale(joueur) or self.diagonale(joueur);

    def tour_joueur(self, joueur):
        player = self.joueur[joueur]['name']
        question = "%s Dans quel colonne souhaites-tu mettre ton jeton ? (Entre 1 et 7) " % player
        colonne = int(input(question)) - 1
        while not self.colonne_libre(colonne) or (colonne < 0 or colonne > 6):
            print("La colonne séléctionnée est pleine.")
            colonne = int(input(question)) - 1
        self.place_jeton(colonne, joueur)
        print(self.print_grille())
        self.tour = 1 if self.tour == 0 else 0