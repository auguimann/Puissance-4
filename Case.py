class Case:

    def __init__(self, col, lig, status=0):

        self.__col = col
        self.__lig = lig
        self.__status = status

    @property
    def col(self) -> int:

        return self.__col

    @property
    def lig(self) -> int:

        return self.__lig

    @property
    def status(self) -> int:

        return self.__status

    @status.setter
    def status(self, newstat):

        self.__status = newstat

    def isFree(self) -> bool:

        return self.__status == 0

    def __str__(self):

        match self.__status:

            case 0:

                return "___"

            case 1:

                return "_🔴_"

            case 2:

                return "_🟡_"
