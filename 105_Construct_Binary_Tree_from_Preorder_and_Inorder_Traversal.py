class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        def helper(left, right):
            nonlocal pre_idx

            if left == right: return None

            root = TreeNode(preorder[pre_idx])
            
            index = idx_map[root.val]

            pre_idx += 1
            root.left = helper(left, index)
            root.right = helper(index + 1, right)

            return root
        
        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder))