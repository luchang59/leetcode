# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        # this recusion helper fuction is going to determine whether a node should be none
        def helper(root):
            if not root: return False
            
            left = helper(root.left)
            right = helper(root.right)
            
            if not left: root.left = None
            if not right: root.right = None
            if not left and not right and root.val == 0:
                return False
            return True
        
        helper(root)
        return root