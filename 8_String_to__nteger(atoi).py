class Solution:
    def myAtoi(self, s):
        string = list(s.strip())
        if not string: return 0
            
        sign = -1 if string[0] == '-' else 1

        if string[0] in ('+', '-'): del string[0]
        
        res, i = 0, 0

        while i < len(string) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        return max(-2**31, min(sign * res, 2**32-1))