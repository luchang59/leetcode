# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# Example 1:
#   input: "69"
#   output: True
# Example 2:
#   input: "962"
#   output: False

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}

        start, end = 0, len(num) - 1

        while start <= end:
            if num[start] not in dic or num[end] not in dic:
                return False
            if num[start] != dic[num[end]]:
                return False
            start += 1
            end -= 1
        
        return True