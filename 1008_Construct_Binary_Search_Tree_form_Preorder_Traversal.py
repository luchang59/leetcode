# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import bisect
class Solution:
    def bstFromPreorder(self, preorder):

        def helper(i, j):
            if i == j: return None
            root = TreeNode(preorder[i])

            # bisect provides support for maintaining a list in sorted order without having to sort the list after each insertion. 
            # bisect.bisect(a, x, lo=0, hi=len(a))
            # find the index at right of x in a[0:len(a)]
            mid = bisect.bisect(preorder, preorder[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(preorder))