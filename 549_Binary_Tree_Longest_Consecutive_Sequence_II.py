# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        self.ans = 0

        def helper(root):
            if not root: return [0, 0]
            
            inc, dec = 1, 1
            left = helper(root.left)
            right = helper(root.right)

            if root.left:
                if root.left.val - 1 == root.val:
                    inc = max(inc, left[0] + 1)
                if root.left.val + 1 == root.val:
                    dec = max(dec, left[[1] + 1])
            if root.right:
                if root.right.val - 1 == root.val:
                    inc = max(inc, right[0] + 1)
                if root.right.val + 1 == root.val:
                    dec = max(dec, right[1] + 1)
            self.ans = max(self.ans, inc + dec - 1)
            return [inc, dec]
        
        helper(root)
        return self.ans