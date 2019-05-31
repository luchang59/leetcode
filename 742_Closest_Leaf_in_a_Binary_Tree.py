# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph, leaves = collections.defaultdict(list), set()
        
        # build the graph
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        

        # use 2 queue to do BFS
        queue = [k]
        while queue:
            next_queue = []
            for node in queue:
                if node in leaves:
                    return node
                next_queue += graph.pop(node, [])
            queue = next_queue