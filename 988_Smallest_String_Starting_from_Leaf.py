# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root: return ""
        
        # Do DFS, find all path, and get the minimum one.
        # how to compare string in python, 'b' > 'a', 'bba' > 'baa'.

        dic = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j',
               10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s',
               19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
        
        res = []
        stack = [(root, [root.val])]
        
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                tmp = ""
                for i in range(len(path)-1, -1, -1):
                    tmp += dic[path[i]]
                res.append(tmp)
            if node.left: stack.append((node.left, path+[node.left.val]))
            if node.right: stack.append((node.right, path+[node.right.val]))
        return min(res)
            
        # recursion
        # do DFS, till no left and right subtree. If reach the leaf node, update teh res.
        def dfs(node, path):
            if not node: return
            path.append(chr(ord('a')+node.val))
            if not node.left and not node.right:
                self.res = min(self.res, ''.join(path)[::-1])
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            del path[-1]
        
        self.res = "{"
        dfs(root, [])
        return self.res