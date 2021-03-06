class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        """
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += 1
        if row + col == self.n - 1:
            self.anti_diag += 1
        if self.n in (self.row[row], self.col[col], self.diag, self.anti_diag):
            return 2
        if -self.n in (self.row[row], self.col[col], self.diag, self.anti_diag):
            return 1
        return 0