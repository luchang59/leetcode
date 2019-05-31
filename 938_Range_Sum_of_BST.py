# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        res = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                res += node.val
            if L < node.val and node.left:
                stack.append(node.left)
            if R > node.val and node.right:
                stack.append(node.right)
                
        return res