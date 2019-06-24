#               1
#               11
#               21
#               1211
#               111221
#               312211
# for every sequence, count the same number from left to right
# example:
# for line 2 is to count line 1, there is one 1
# result is 11
# for line 3 is to count line 2, there is two 1
# result is 21
# for line 4 is to count line 3, there is one 2 and one 1
# result is 1211

class Solution:
    def countAndSay(self, n):

        s = '1'

        for _ in range(n - 1):
            prev, curr, count = s[0], "", 0
            for l in s:
                if l == prev:
                    count += 1
                else:
                    curr += str(count) + prev
                    prev = l
                    count = 1
            curr += str(count) + prev
            s = curr

        return s