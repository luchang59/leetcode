class Solution:
    def rotate(self, matrix):
        N = len(matrix)

        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][j] = matrix[j][i], matrix[i][j]
        
        for i in range(N):
            matrix[i].reverse()