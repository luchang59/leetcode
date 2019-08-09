import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root: return []

        res = []
        queue = collections.deque([root])

        while queue:
            pos = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()
                if i == pos: res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return res