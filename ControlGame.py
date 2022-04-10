class ControlGame:
    turnsToPlay = None
    turns = 0
    player = None
    MAX_TURNS = 64
    board = [['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.']]
    def __init__(self, turnsToPlay= MAX_TURNS):
        self.board = [['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.']]
        self.player = "Red"
        self.turns = 0
        self.turnsToPlay = turnsToPlay

    def __str__(self):
        return "Current board is:\n  0 1 2 3 4 5 6 7\n0 {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]} {self.board[0][4]} {self.board[0][5]} {self.board[0][6]} {self.board[0][7]}\n1 {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} {self.board[1][4]} {self.board[1][5]} {self.board[1][6]} {self.board[1][7]}\n2 {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]} {self.board[2][4]} {self.board[2][5]} {self.board[2][6]} {self.board[2][7]}\n3 {self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]} {self.board[3][4]} {self.board[3][5]} {self.board[3][6]} {self.board[3][7]}\n4 {self.board[4][0]} {self.board[4][1]} {self.board[4][2]} {self.board[4][3]} {self.board[4][4]} {self.board[4][5]} {self.board[4][6]} {self.board[4][7]}\n5 {self.board[5][0]} {self.board[5][1]} {self.board[5][2]} {self.board[5][3]} {self.board[5][4]} {self.board[5][5]} {self.board[5][6]} {self.board[5][7]}\n6 {self.board[6][0]} {self.board[6][1]} {self.board[6][2]} {self.board[6][3]} {self.board[6][4]} {self.board[6][5]} {self.board[6][6]} {self.board[6][7]}\n7 {self.board[7][0]} {self.board[7][1]} {self.board[7][2]} {self.board[7][3]} {self.board[7][4]} {self.board[7][5]} {self.board[7][6]} {self.board[7][7]}".format(self=self)

    def getCurrentPlayer(self):
        return self.player

    def swapCurrentPlayer(self):
        if self.player=="Red":
            self.player="Blue"
        else:
            self.Player="Red"

    def getBoardState(self):
        return "Current board is:\n  0 1 2 3 4 5 6 7\n0 {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]} {self.board[0][4]} {self.board[0][5]} {self.board[0][6]} {self.board[0][7]}\n1 {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} {self.board[1][4]} {self.board[1][5]} {self.board[1][6]} {self.board[1][7]}\n2 {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]} {self.board[2][4]} {self.board[2][5]} {self.board[2][6]} {self.board[2][7]}\n3 {self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]} {self.board[3][4]} {self.board[3][5]} {self.board[3][6]} {self.board[3][7]}\n4 {self.board[4][0]} {self.board[4][1]} {self.board[4][2]} {self.board[4][3]} {self.board[4][4]} {self.board[4][5]} {self.board[4][6]} {self.board[4][7]}\n5 {self.board[5][0]} {self.board[5][1]} {self.board[5][2]} {self.board[5][3]} {self.board[5][4]} {self.board[5][5]} {self.board[5][6]} {self.board[5][7]}\n6 {self.board[6][0]} {self.board[6][1]} {self.board[6][2]} {self.board[6][3]} {self.board[6][4]} {self.board[6][5]} {self.board[6][6]} {self.board[6][7]}\n7 {self.board[7][0]} {self.board[7][1]} {self.board[7][2]} {self.board[7][3]} {self.board[7][4]} {self.board[7][5]} {self.board[7][6]} {self.board[7][7]}\n".format(self=self)

    def takeTurn(self, row, col):
        self.turns+=1
        if (self.board[row][col]=='.' and row<8 and col<8):
            if self.player=="Red":
                self.board[row][col]='R'
                self.player="Blue"
            else:
                self.board[row][col] = 'B'
                self.player="Red"
            return True
        else:
            return False

    def getScore(self):
        red = blue = sred = sblue = adjred = adjblue = 0
        for i in range (8):
            for j in range (8):
                if self.board[i][j]=='R':
                    red+=1
                elif self.board[i][j]=='B':
                    blue+=1
            if red>blue:
                sred+=1
            elif blue>red:
                sblue+=1
            red=blue=0

        for i in range (8):
            for j in range (8):
                if self.board[j][i]=='R':
                    red+=1
                elif self.board[j][i]=='B':
                    blue+=1
            if red>blue:
                sred+=1
            elif blue>red:
                sblue+=1
            red=blue=0

        for i in range(2,6):
            for j in range(2,6):
                if self.board[i][j] == 'R':
                    if self.board[i+1][j]=='R' or self.board[i-1][j]=='R' or self.board[i][j+1]=='R' or self.board[i][j-1]=='R':
                        adjred+=1
                if self.board[i][j] == 'B':
                    if self.board[i+1][j]=='B' or self.board[i-1][j]=='B' or self.board[i][j+1]=='B' or self.board[i][j-1]=='B':
                        adjblue+=1
        for i in range (7):
            if self.board[i][0] == 'R':
                if self.board[i + 1][0] == 'R' or self.board[i - 1][0] == 'R' or self.board[i][0 + 1] == 'R':
                    adjred += 1
            if self.board[i][0] == 'B':
                if self.board[i+1][0]=='B' or self.board[i-1][0]=='B' or self.board[i][0+1]=='B':
                    adjblue+=1
            if self.board[i][7] == 'R':
                if self.board[i + 1][7] == 'R' or self.board[i - 1][7] == 'R' or self.board[i][7 - 1] == 'R':
                    adjred += 1
            if self.board[i][7] == 'B':
                if self.board[i+1][7]=='B' or self.board[i-1][7]=='B' or self.board[i][7-1]=='B':
                    adjblue+=1
        for j in range (7):
            if self.board[0][j] == 'R':
                if self.board[0 + 1][j] == 'R' or self.board[0][j + 1] == 'R' or self.board[0][j - 1] == 'R':
                    adjred += 1
            if self.board[7][j] == 'B':
                if self.board[7 - 1][j] == 'B' or self.board[7][j + 1] == 'B' or self.board[7][j - 1] == 'B':
                    adjblue += 1
        sred += adjred/2
        sblue += adjblue/2
        return int(sred),int(sblue)
