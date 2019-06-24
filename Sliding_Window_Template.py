class Solution:
    def template(self, s: str, t: str):

        result = []
        if len(t) > len(s): return result
        
        dic = {}

        for c in t:
            if dic[c]: dic[c] += 1
            else: dic[c] = 1
        
        counter = len(dic)

        begin, end = 0, 0

        length = float('inf')

        while end < len(s):

            c = s[end]
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    counter -= 1
            end += 1

            while counter == 0:
                tempc = s[begin]
                if tempc in dic:
                    dic[tempc] += 1
                    if dic[tempc] > 0:
                        counter += 1
                begin += 1
        
        return result