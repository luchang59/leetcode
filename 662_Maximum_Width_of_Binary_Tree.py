# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        queue = collections.deque([(root, 0)])
        res = 1

        while queue:
            start = queue[0][1]
            end = queue[-1][1]
            res = max(res, end - start + 1)
            
            for _ in range(len(queue)):
                node, pos = queue.popleft()
                if node.left: queue.append((node.left, pos * 2))
                if node.right: queue.append((node.right, pos * 2 + 1))
                
        return res