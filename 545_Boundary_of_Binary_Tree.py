# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode): # -> List[int]:
        if not root: return []
        # for this problem, I set 3 fuction to find the left boundary, leave and right boundary.
        # then combine them together.
        # it should be noticed if root has no left subtree or no right subtree.
        def getLeftPath(root):
            stack = [(root, [root.val])]
            while stack:
                node, path = stack.pop()
                if not node.left and not node.right:
                    break
                if node.right:
                    stack.append((node.right, path+[node.right.val]))
                if node.left:
                    stack.append((node.left, path+[node.left.val]))
            return path
        
        def getRightPath(root):
            stack = [(root, [root.val])]
            while stack:
                node, path = stack.pop()
                if not node.left and not node.right:
                    break
                if node.left:
                    stack.append((node.left, path+[node.left.val]))
                if node.right:
                    stack.append((node.right, path+[node.right.val]))
            return path[:0:-1]
    
        def getleavfPath(root):
            res = []
            stack = [root]
            while stack:
                node = stack.pop()
                if not node.right and not node.left:
                    res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return res
        
        if not root.left:
            return [root.val] + getleavfPath(root)[:-1] + getRightPath(root)
        
        if not root.right:
            return getLeftPath(root) + getleavfPath(root)[1:]
        
        return getLeftPath(root) + getleavfPath(root)[1:-1] + getRightPath(root)
        
        