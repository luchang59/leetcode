# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode):
        
        def get_height(node):
            if not node: return 0
            
            left = get_height(node.left)
            right = get_height(node.right)
            
            return 1 + max(left, right)
        
        def update_output(node, row, left, right):
            if not node: return
            mid = (left + right) // 2
            # use recursion to update the output
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1 , left, mid - 1)
            update_output(node.right, row + 1 , mid + 1, right)
        
        height = get_height(root)
        # the tree wide is 2^height of the tree minus 1
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        update_output(root, 0, 0, width - 1)
        return self.output


        #      1
        #     / \
        #    2   3
        #   / \ / \
        #  4   56  7