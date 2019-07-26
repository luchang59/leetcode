class Solution:
    def partitionLabels(self, S):

        dic = {c: i for i, c in enumerate(S)}

        count = j = 0
        res = []

        for i, c in enumerate(S):
            count += 1
            j = max(j, dic[c])

            if i == j:
                res.append(count)
                count = 0
        
        return res 