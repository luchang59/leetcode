class Solution:
    def isValid(self, s):
        stack = []
        dic = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in dic.keys():
                s.append(char)
            elif char in dic.values():
                if stack == [] or char != dic[stack.pop()]:
                    return False
            else:
                return False
        
        return stack == []