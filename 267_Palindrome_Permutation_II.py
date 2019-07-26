import collections

class solution:
    def generatePalindrome(self, s: str):

        res, odd, even = [], "", ""
        count = collections.Counter(s)

        for c in count:
            if count[c] % 2 != 0:
                odd += c
            if count[c] > 1:
                even += c * (count[c] // 2)

        if len(odd) > 1: return res
        
        def backtrack(string, path):
            if not string:
                res.append(path + odd + path[::-1])
                return 
            for i in range(len(string)):
                if i > 0 and string[i] == string[i - 1]: continue
                backtrack(string[:i] + string[i + 1:], path + string[i])
        
        backtrack(even, "")
        return res