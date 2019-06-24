# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def helper(root, target):
            stack = [(root, None, 0)]
            
            while stack:
                node, parent, depth = stack.pop()
                if node:
                    if node.val == target:
                        return parent, depth
                    stack.append((node.left, node, depth + 1))
                    stack.append((node.right, node, depth + 1))
        
        return helper(root, x)[0] != helper(root, y)[0] and helper(root, x)[1] == helper(root, y)[1]
         