"""
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.
Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:
Input: A = "ab", B = "ba"
Output: 1

Example 2:
Input: A = "abc", B = "bca"
Output: 2

Example 3:
Input: A = "abac", B = "baca"
Output: 2

Example 4:
Input: A = "aabc", B = "abca"
Output: 2

Note:
1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
"""

import collections
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        if A == B: return 0

        queue = collections.deque([(A, 0)])
        seen = set([A])

        def swap(string, i, j):
            lst = list(string)
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)

        while queue:
            node, step = queue.popleft()
            i = 0
            while node[i] == B[i]: i += 1
            for j in range(i + 1, len(A)):
                if node[j] == B[j] or node[i] != B[j]: continue
                nxt = swap(node, i, j)
                if nxt == B: return step + 1
                if nxt not in seen:
                    queue.append((nxt, step + 1))
                    seen.add(node)