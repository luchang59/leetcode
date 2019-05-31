# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        # iteration version, build the ascending list and find the k-1th element in this list.
        if not root: return None
        
        res = []
        stack = [root]
        cur = root
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res[k-1]
    
        # use recursion to build the list, left + root + right
        def inorder(root):
            if not root: return []
            
            left = inorder(root.left)
            right = inorder(root.right)
            
            return left + [root.val] + right
        
        return inorder(root)[k - 1]