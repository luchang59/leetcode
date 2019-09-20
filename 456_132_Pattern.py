"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]
Output: False
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]
Output: True
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]
Output: True
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

class Solution:
    def find132pattern(self, nums) -> bool:
        """
        单调栈：单调递减栈
        存两个值：前i个数字中的最小值，当前递减趋势中的最小值
        例如： [2, 3, 5, 4, 3, 2]
        当到 4 的位置时候，栈内存的是 [5, 4]
        """

        mini = float('inf')
        stack = []

        for num in nums:
            while stack and stack[-1][0] <= num: stack.pop()
            if stack and stack[-1][1] < num: return True
            mini = min(mini, num)
            stack.append((num, mini))
        
        return False