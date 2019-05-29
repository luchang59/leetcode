# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder: return None
        
        val = postorder.pop()
        root = TreeNode(val)
        if len(inorder) == 1: return root
        # Because the list at the left of root in inorder is the left subtree, right list as well.
        # Therefore, if we can find the root's index, we can split the list to left and right part.
        i = inorder.index(val)
        
        root.right = self.buildTree(inorder[i+1:], postorder)
        root.left = self.buildTree(inorder[:i], postorder)
        
        return root
        