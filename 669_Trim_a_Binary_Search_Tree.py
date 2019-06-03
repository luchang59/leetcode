# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        
        def helper(root):
            if not root: return None
            
            if root.val > R:
                return helper(root.left)
            
            if root.val < L:
                return helper(root.right)
            
            root.left = helper(root.left)
            root.right = helper(root.right)
            return root
    
        return helper(root)