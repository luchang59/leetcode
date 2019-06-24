# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False
        stack = [root]
        dic = {}
        while stack:
            node = stack.pop()
            if node:
                if node.val in dic: return True
                else:
                    dic[k - node.val] = node
                    stack.append(node.left)
                    stack.append(node.right)
        return False