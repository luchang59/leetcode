# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        """
        for recursion, if no root or root.val < val, create a new node. and the node.left is root
        else, root.right uses the function again, the arguments is the root.right and val.
        untill find the suitable node.
        """
        if not root or root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
        
        # use While-Loop
        # prev, cur = None, root
        # while cur and cur.vasl > val:
        #     prev, cur = cur, cur.right
        # node = TreeNode(val)
        # node.left = cur
        # if prev: prev.right = node
        # return root if root.val > val else node