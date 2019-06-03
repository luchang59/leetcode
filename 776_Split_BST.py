# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int):
        
        if not root: return None, None
        
        if root.val <= V:
            small, large = self.splitBST(root.right, V)
            root.right = small
            return root, large
        
        small, large = self.splitBST(root.left, V)
        root.left = large
        return small, root