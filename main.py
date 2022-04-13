def Affichage(grille):
    string = " __1__ __2__ __3__ __4__ __5__ __6__ __7__\n"
    for i in range(len(grille)):
        string=string+"|_"
        for col in range(len(grille[0])):
            if (col != 0):
                string = string + "_|_"

            if grille[i][col]==0:
                string=string+ "___"
            elif grille[i][col]==1:
                string=string+ " X "
            elif grille[i][col]==-1:
                string=string+ " O "
        string = string + "_|"
        string=string+"\n"
    print(string)

def CheckPosition(grille, col):
    caseL=False
    for i in range(len(grille)):
        if grille[i][col]==0:
            caseL=True
            break
    return caseL

grille=[[0] * 7 for i in range(6)]
Affichage(grille)