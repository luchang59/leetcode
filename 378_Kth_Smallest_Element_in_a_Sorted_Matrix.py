class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        
        mini, maxi = matrix[0][0], matrix[-1][-1]
        N = len(matrix)
        
        while mini < maxi:
            mid = (mini + maxi) // 2
            count = 0
            j = len(matrix[0]) - 1
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            # print(count)
            if count < k:
                mini = mid + 1
            else:
                maxi = mid
        return mini 