"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
Note:
A subtree must include all of its descendants.

Example:
Input: [10,5,15,1,8,null,7]
"""
#    10 
#    / \
#   5  15 
#  / \   \
# 1   8   7
"""
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.

Follow up: Can you figure out ways to solve it with O(n) time complexity?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root: return 0

        self.res = 1

        def helper(node):
            if not node: return 0, float('inf'), float('-inf')

            left, min_l, max_l = helper(node.left)
            right, min_r, max_r = helper(node.right)

            if max_l < node.val < min_r:
                self.res = left + 1 + right
                return left + 1 + right, min(min_l, node.val), max(max_r, node.val)
            return 0, float('-inf'), float('inf')
                
        helper(root)
        return self.res