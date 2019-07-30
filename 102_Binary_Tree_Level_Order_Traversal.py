import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        # Iteration Solution:
            # Time complexity: O(N)
            # Space complexity: O(N)
        
        res = []
        if not root: return res

        queue = collections.deque()
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        
        return res

        # Recursion Solution:
            # Time complexity: O(N)
            # Space complexity: O(N)
        
        # res = []
        # if not root: return res

        # def helper(node, level):
        #     if level == len(res):
        #         res.append([])
        #     res[level].append(node.val)
        #     if node.left: helper(node.left, level + 1)
        #     if node.right: helper(node.right, level + 1)
        
        # helper(root, 0)
        # return res