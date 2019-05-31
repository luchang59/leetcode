class Solution:
    def flipAndInvertImage(self, A):
        """
        Brute Force
        I write 2 functions, flip and invert, then for loop the A, do this two funciton.
        """
        def flip(horizontal):
            start, end = 0, len(horizontal) - 1
            while start < end:
                horizontal[start], horizontal[end] = horizontal[end], horizontal[start]
                start += 1
                end -= 1
                
            return horizontal
        
        def invert(vertical):
            for i in range(len(vertical)):
                vertical[i] ^= 1
            return vertical
        
        for a in A:
            a = flip(a)
            a = invert(a)
            
        return A