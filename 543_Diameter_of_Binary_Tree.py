# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        # we need to traverse all nodes in the tree and get their sum of left subtree depth and right subtree depth.
        self.maxPath = 0
        self.helper(root)
        return self.maxPath
    
    def helper(self, root):
        """
        This function can find the max depth of a tree and update the maxPath, while considering the left depth added right path.
        """
        if not root: return 0
        
        # this recursion is to travese all node in this tree.
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        # this part is the core, it sum the left and right depth. And compare the maxPath and new Value
        path = left + right
        self.maxPath = max(self.maxPath, path)
        
        return max(left, right) + 1