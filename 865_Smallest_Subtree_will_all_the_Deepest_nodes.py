# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root: return 0, None
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left[0] > right[0]: return left[0] + 1, left[1]
            if left[0] < right[0]: return right[0] + 1, right[1]
            return left[0] + 1, root
        
        return dfs(root)[1]