class Solution:
    def StrStr(self, haystack, needle):
        if not needle: return 0

        H = len(haystack)
        N = len(needle)

        for i in range(H - N + 1):
            if haystack[i:i+N] == needle:
                return i
        return -1