class Solution:
    def exist(self, board, word: str) -> bool:
        
        def backTrack(row, col, w):
            if len(w) == 0: return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != w[0]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'
            res = backTrack(row - 1, col, w[1:]) or backTrack(row + 1, col, w[1:]) or backTrack(row, col - 1, w[1:]) or backTrack(row, col + 1, w[1:])
            board[row][col] = temp

            return res 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backTrack(i, j, word): return True
        return False
