# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root: return root
        # this case is for d = 1, insert the node at first level, and it left node is root.
        if d == 1:
            head = TreeNode(v)
            head.left = root
            return head
        
        queue = collections.deque()
        queue.append((root, 1))
        row = []
        # this while loop is for finding the d - 1 level, because the nodes' left and right is new node.
        while queue:
            node, depth = queue.popleft()
            if depth == d - 1:
                row.append(node)
                if queue[0][1] != d - 1:
                    break
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
                
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
            
        return root
                