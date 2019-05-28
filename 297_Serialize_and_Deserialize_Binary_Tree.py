# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # I used while-loop for traverse the root, and transfer it to string. Used Preorder traverse
        if not root: return '#'
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append('#')
        return ' '.join(res)
        # This is the recursive version
        # def helper(node):
        #     if node:
        #         res.append(str(node.val))
        #         helper(node.left)
        #         helper(node.right)
        #     else:
        #         res.append('#')
        # res = []
        # helper(root)
        # return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # I don't know how to use while-loop to convert the string to tree.
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            # get the first node of the queue
            node = l.popleft()
            # if the node value is #, don't do anything
            if node == '#':
                return None
            # if the node value is int, built the root, and use the fuction to build the left node and right node.
            root = TreeNode(node)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            # return the root
            return root
        # deque the original data
        data_list = collections.deque(data.split())
        root = rdeserialize(data_list)
        return root
       
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))