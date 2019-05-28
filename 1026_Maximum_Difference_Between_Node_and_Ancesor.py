# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0
        # store the maximum and minimum value thought the DFS path
        stack = [(root, root.val, root.val)]
        res = 0
        while stack:
            node, curMax, curMin = stack.pop()
            if node:
                if node.val > curMax:
                    curMax = node.val
                if node.val < curMin:
                    curMin = node.val
                res = max(res, curMax - curMin)
                stack.append((node.left, curMax, curMin))
                stack.append((node.right, curMax, curMin))
                
        return res