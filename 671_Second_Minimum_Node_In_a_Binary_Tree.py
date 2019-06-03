# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        
        seen = set()
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                seen.add(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        if len(seen) == 1: return -1
        return sorted(seen)[1]