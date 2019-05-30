# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        """
        actually, it is still a question about preorder traversal, just add '()' in every preorder.
        just notice that, 
        """
#         if not t: return ""
#         res = ""
#         stack = [t]
#         while stack:
#             node = stack.pop()
#             if node == ')':
#                 res += ')'
#                 continue
#             res += "(" + str(node.val)
#             if not node.left and node.right:
#                 res += "()"
#             if node.right:
#                 stack.append(")")
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(")")
#                 stack.append(node.left)

#         return res[1:]
    
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)
