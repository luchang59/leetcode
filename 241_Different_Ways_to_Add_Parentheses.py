class Solution:
    def diffWaysToCompute(self, input):

        if input.isdigit(): return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for r1 in res1:
                    for r2 in res2:
                        res.append(self.helper(r1, r2, input[i]))
        return res

    def helper(self, i, j, operator):
        if operator == '+': return i + j
        if operator == '-': return i - j
        if operator == '*': return i * j