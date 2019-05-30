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
        # This part is to use postorder to convert the tree.
        # def postorder(root):
        #     if not root: return []
        #     left = postorder(root.left)
        #     right = postorder(root.right)
        #     return left + right + [root.val]

        # return ' '.join(map(str, postorder(root)))

        # This part is to use preorder to convert the tree.
        def preorder(root):
            if not root: return []
            left = preorder(root.left)
            right = preorder(root.right)
            return [root.val] + left + right
        
        return ' '.join(map(str, preorder(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # this part is to deserialize based on preorder, noticed that we must do left first then right.
        # pop the head node of list
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[0] < lower or data[0] > upper:
                return None
            
            val = data.popleft()
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        
        # this part is to deserialize based on preorder, noticed that we must do right first then left.
        # pop the tail node of list
#         def helper(lower = float('-inf'), upper = float('inf')):
#             if not data or data[-1] < lower or data[-1] > upper:
#                 return None
            
#             val = data.pop()
#             root = TreeNode(val)
#             root.right = helper(val, upper)
#             root.left = helper(lower, val)
#             return root
        
        data = [int(x) for x in data.split(' ') if x]
        data = collections.deque(data)
        return helper()

        # data = [int(x) for x in data.split(' ') if x]
        # inorder = sorted(data)

        # this part is to sort postorder list to make a inorder list, then based on inorder and postorder to make tree. Just like 106
        # def helper(inorder, postorder):
        #     if not inorder or not postorder: return None
        #     val = postorder.pop()
        #     root = TreeNode(val)
        #     if len(inorder) == 1: return root
        #     i = inorder.index(val)
        #     root.right = helper(inorder[i+1:], postorder)
        #     root.left = helper(inorder[:i], postorder)
        #     return root
        # return helper(inorder, data)
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))