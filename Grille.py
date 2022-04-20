from json.tool import main
from Case import Case

class Grille :
    nbcol, nblig = 7,6
    def __init__(self) -> None:
        nbcol, nblig = 7,6
        
        self.grille = [["" for x in range(nbcol)] for y in range(nblig)]

        for lig in range(nblig):

            for col in range(nbcol):

                self.grille[lig][col] = Case(col,lig)
    
    def __str__(self) -> str:

        str = "|_1____2____3____4____5____6____7_|\n"
        for lig in range(6):
            for col in range(7):
                str += f"|{self.grille[lig][col]}|"
            str += "\n"
        return str

    # verrification de la possibilité d'ajouter un pion a une colonne 
    def PositionLibre(self,col):
        caseLibre=False
        for lig in range(self.nblig):
            if self.grille[lig][col].status == 0:
                caseLibre=True
                break
        return caseLibre

if __name__ == '__main__':
    test = Grille()
    print(test)
    print(Grille.PositionLibre(test,1))