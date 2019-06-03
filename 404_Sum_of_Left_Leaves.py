# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # recursive version
        if not root: return 0
        # notice, here use root.left to know this node is left node, determine whether this node is suitable.
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        
        # iterative version
        if not root: return 0
        
        res = 0
        stack = [(root, None)]
        while stack:
            node, flag = stack.pop()
            if not node.left and not node.right and flag == 'L':
                res += node.val
            if node.left:
                stack.append((node.left, 'L'))
            if node.right:
                stack.append((node.right, 'R'))
                
        return res