# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        
        self.ans = 0
        
        def helper(root):
            if not root: return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            self.ans += abs(left) + abs(right)
            
            return left + root.val + right - 1
        
        helper(root)
        return self.ans