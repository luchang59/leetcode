# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def helper(root):
            if not root: return "$"
            left = helper(root.left)
            right = helper(root.right)
            return  "^" + str(root.val) + "#" + left + right
        
        sRes = helper(s)
        tRes = helper(t)
        print(sRes, tRes)
        
        return tRes in sRes