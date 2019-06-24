class Solution:
    def letterCombinations(self, digits: str):

        
        if not digits: return []
        
        letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = []
        def backtrack(digit, path):
            if len(digit) == 0:
                res.append(path)
                return
            for c in letter[digit[0]]:
                backtrack(digit[1:], path + c)
        
        backtrack(digits, '')
        return res