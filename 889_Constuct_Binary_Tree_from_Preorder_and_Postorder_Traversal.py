class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):

        if not pre or not post: return None

        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        idx = post.index(pre[1]) + 1

        root.left = self.constructFromPrePost(pre[1:idx + 1], post[:idx])
        root.right = self.constructFromPrePost(pre[idx + 1:], post[idx:-1])