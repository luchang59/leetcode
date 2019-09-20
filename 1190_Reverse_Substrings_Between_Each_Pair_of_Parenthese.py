"""
Given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any bracke.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        string = ''

        for char in s:
            if char.isalpha():
                string += char
            elif char == '(':
                stack.append(string)
                stack.append('(')
                string = ''
            else:
                while stack[-1] != '(':
                    string = stack.pop() + string
                string = string[::-1]
                stack.pop()
                if stack:
                    stack[-1] += string
                else:
                    stack.append(string)
                string = ''