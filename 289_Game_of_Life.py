class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

    # ------ O(MN) Space ------

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        copyBoard = [[board[row][col] for col in range(len(board[0]))] for row in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and copyBoard[i][j] == 1:
                        count += 1
                if count < 2 or count > 3:
                    board[i][j] = 0
                elif count == 3:
                    board[i][j] = 1
    
    # ------ O(1) Space ------
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and abs(board[ni][nj]) == 1:
                        count += 1
                if board[i][j] == 1 and count not in (2, 3):
                    board[i][j] = -1
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0