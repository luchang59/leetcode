# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root: return []

        res = []

        def helper(root):
            # if not root.left and not root.right:
            #     res.append(root.val)
            #     return
            # if root.left:
            #     left = helper(root.left)
            # res.append(root.val)
            # if root.right:
            #     right = helper(root.right)
            if root:
                if root.left:
                    helper(root.left)
                res.append(root.val)
                if root.right:
                    helper(root.right)
        
        helper(root)
        return res

        # ---- iteration solution -----

        if not root: return []

        res = []
        curr, stack = root, []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res