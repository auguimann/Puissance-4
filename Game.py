from Grille import Grille
from Joueur import Joueur
from Case import Case

class Game:
    def __init__(self):
        self.plateau = Grille()
        self.joueur1 = Joueur("Augustin")
        
    def start_game(self):
        ...
        
    def jouerCoup(self, col : int, joueur : int):
        """Permet de jouer un coup

        Args:
            col (int): Colonne sur laquelle on veut jouer un coup
            joueur (int): id du jouer soit 1 ou 2
        """
        
        if not self.plateau.get_case(0, col-1).isFree():
            print("Erreur, col pleine")
            return
        for i in range(6)[::-1]:
            if self.plateau.get_case(i, col-1).isFree():
                self.plateau.get_case(i, col-1).state = joueur
                break
        print(self.plateau)
        
    def verifCoupGagnant(self):
        ...
        
if __name__ == "__main__":
    jeu = Game()
    jeu.jouerCoup(2, 1)
    jeu.jouerCoup(2,2)
    jeu.jouerCoup(2,1)
    jeu.jouerCoup(2,2)
    jeu.jouerCoup(2,1)
    jeu.jouerCoup(2,2)
    jeu.jouerCoup(2,1)