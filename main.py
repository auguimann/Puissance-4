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

infini=10000

def maxValue(grille, n, depth, joueur):
    v = -infini
    if TerminalTest(grille):
        return Utility(grille)
    elif (n > depth):
        return 0
    else:
        for a in Actions(grille):
            v = max(v, minValue(Result(grille, a, joueur), n + 1, depth, ChangementJoueur(joueur)))
        return v

def minValue(grille, n, depth, joueur):
    v = infini
    if TerminalTest(grille):
        return Utility(grille)
    elif (n > depth):
        return 0
    else:
        nb = 0
        for a in Actions(grille):
            nb = nb + 1
            v = min(v, maxValue(Result(grille, a, joueur), n + 1, depth, ChangementJoueur(joueur)))
        return v

def minimaxDecision(grille, depth, joueur):
    ListeActions, ListeUtility = [], []
    for a in Actions(grille):
        ListeActions.append(a)
        if TerminalTest(Result(grille, a, joueur)):
            ListeUtility.append(Utility(Result(grille, a, joueur)))
        else:
            ListeUtility.append(minValue(Result(grille, a, joueur), 1, depth, ChangementJoueur(joueur)))
    print(ListeUtility)
    for i in range(len(ListeActions)):
        if ListeUtility[i] == max(ListeUtility):
            #on retourne l'action dont l'utility est maximale
            return ListeActions[i]


infini=10000
grille=[[0] * 7 for i in range(6)]
Affichage(grille)