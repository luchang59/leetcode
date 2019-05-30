# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        what did this function do?
        just to find if p, q in subtree.
        if just one of nodes under root, return True
        if both side return True, means left side and right side include one of nodes. Therefore the ancestor is the root.
        """

        
        if not root or root == q or root == p:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right
        
        return None
        