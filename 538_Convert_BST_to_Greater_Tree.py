# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # recursion, because we need to add total value of the node which larger than this node.
        # so we need use a total to record it.
        self.total = 0
        def helper(root):
            if root:
                helper(root.right)
                self.total = root.val = self.total + root.val
                helper(root.left)
        helper(root)
        return root
        
        
        
        total = 0
        
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            
            cur = stack.pop()
            total += cur.val
            cur.val = total
            cur = cur.left
            
        return root