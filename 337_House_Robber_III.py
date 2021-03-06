# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.robDFS(root)[1]
    
    def robDFS(self,node):
        if node is None:
            return (0,0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        # the first element stores the value of subtree sum
        # the second element stores the maximum value betweent substree sum and root add subsubtree.
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))