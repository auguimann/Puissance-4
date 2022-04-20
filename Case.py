# 0 libre 
# 1 rouge 
# 2 jaune
#pour les status possibles

class Case:

    def __init__(self, col, lig, state=0):

        self.__col = col
        self.__lig = lig
        self.__state = state

    @property
    def col(self) -> int:

        return self.__col

    @property
    def lig(self) -> int:

        return self.__lig

    @property
    def status(self) -> int:

        return self.__state

    @status.setter
    def status(self, newstat):

        self.__state = newstat

    def isFree(self) -> bool:

        return self.__state == 0

    def __str__(self) -> str:

        match self.__state:

            case 0:

                return "___"

            case 1:

                return "_🔴_"

            case 2:

                return "_🟡_"
