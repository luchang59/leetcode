# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # Different from inorder, the root in preorder is the first one. But we can know that the second one is the root of left substree.
        # And the second one in inorder list is the last one of a tree in postorder, so we can use it to split them.s
        if not pre or not post: return None
        
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root