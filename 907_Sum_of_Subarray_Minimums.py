"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
Since the answer may be large, return the answer modulo 10^9 + 7.
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""

class Solution:
    def sumSubarrayMins(self, A):
        """
        对于前i个与元素来说，所有subarray的最小值的和，如果a[i]比之前某个元素小，那么需要将之前的结果更新
        res[i] = res[i-1] - c1 * v1 - c2 * v2 - ... - cn * vn + (c1 + c2 + c3 + ... + cn) * v[i]
        """

        if not A: return 0

        Mod = 10 ** 9 + 7
        res, curSum = 0, 0
        stack = []

        for a in A:
            count = 1
            while stack and stack[-1][0] >= a:
                v, c = stack.pop()
                curSum -= v * c
                count += c
            stack.append((a, count))
            curSum += a * count
            res += curSum
        
        return res % Mod