# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)

        connect(None, root)
        bfs = [target.val]
        
        queue1 = collections.deque(bfs)
        queue2 = collections.deque()
        seen = set()

        while K:
            while queue1:
                node = queue1.popleft()
                seen.add(node)
                for nei in conn[node]:
                    if nei not in seen:
                        queue2.append(nei)
            queue1, queue2 = queue2, queue1
            K -= 1
        res = []

        for q in queue1:
            res.append(q)

        return res