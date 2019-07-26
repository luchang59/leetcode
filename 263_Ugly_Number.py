class Solution:
    def isUgly(self, num):

        if num <= 0: return False
        if num in (1, 2, 3, 5): return True
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0: return False

        return self.isUgly(num / 2) or self.isUgly(num / 3) or self.isUgly(num / 5)