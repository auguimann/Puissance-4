from json.tool import main
from case import Case

class Grille :
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

if __name__ == '__main__':
    test = Grille()
    print(test)