class Solution:
    def nextGreaterElement(self, n):

        lst = list(map(int, str(n)))
        i = len(lst) - 2
        while i >= 0 and lst[i+1] <= lst[i]:
            i -= 1
        
        if i < 0: return -1
        
        j = len(lst) - 1
        while j >= 0 and lst[j] <= lst[i]:
            j -= 1
        lst[i], lst[j] = lst[j], lst[i]
        lst[i+1:] = reversed(lst[i+1:])
        res = int("".join(map(str, lst)))
        return res if res <= 1<<31 -1 else -1