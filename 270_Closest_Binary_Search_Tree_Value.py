# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        path = []
        while root:
            path += [root.val]
            root = root.left if target < root.val else root.right
        
        return min(path, key=lambda x: abs(target - x))

        # use inorder travese, get the ascending list, then calculate the distance.
        def inorder(root):
            if not root: return []
            
            left = inorder(root.left)
            right = inorder(root.right)
            
            return left + [root.val] + right
    
        res = inorder(root)
        minimum = float('inf')
        for r in res:
            if abs(r - target) < minimum:
                minimum = abs(r - target)
                ans = r
        return ans