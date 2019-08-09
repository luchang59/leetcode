# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True

        res = []
        queue = collections.deque([(root, 1)])

        while queue:
            node, pos = queue.popleft()
            res.append(pos)
            if node.left: queue.append((node.left, pos * 2))
            if node.right: queue.append((node.right, pos * 2 + 1))
        
        return res[-1] == len(res)