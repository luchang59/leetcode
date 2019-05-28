# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # It actually didn't change the tree, it just store the node which have empty left or right node.
        # This function uses deque to store the node by level top to down and left to right order.
        self.deque = collections.deque()
        self.root = root
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        # insert new node to the first node of deque, and if right node is filled, pop this node.
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        # just return the root
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()