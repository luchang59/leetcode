"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: "bcabc"
Output: "abc"

Example 2:
Input: "cbacdcbc"
Output: "acdb"
"""

import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        count = collections.Counter(s)
        seen = set()

        for char in s:
            if char not in seen:
                while stack and stack[-1] > char:
                    top = stack[-1]
                    if count[top] == 1: break
                    top = stack.pop()
                    count[top] -= 1
                    seen.remove(top)
                stack.append(char)
                seen.add(char)
            else:
                count[char] -= 1
        
        return ''.join(stack)

