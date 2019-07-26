class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def generateTrees(self, n):

        if n == 0: return []

        def dfs(lst):
            if not lst: return [None,]
            
            res = []
            for i in range(len(lst)):
                for left in dfs(lst[:i]):
                    for right in dfs(lst[i + 1:]):
                        root = TreeNode(lst[i])
                        root.left = left
                        root.right = right
                        res.append(root)
        
        return dfs([i for i in range(1, n + 1)])