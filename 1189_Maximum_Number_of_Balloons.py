"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
"""
import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        res = float('inf')

        for char in 'balon':
            if char in ('l', 'o'):
                res = min(res, count[char] // 2)
            else:
                res = min(res, count[char])
        
        return res