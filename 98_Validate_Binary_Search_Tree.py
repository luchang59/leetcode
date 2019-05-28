# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, lower_bound, upper_bound):
        # lower_bound means the node.val must be larger than it, upper_bound means the node.val must be smaller than the upper_bound
        if not node: return True
        # if node.val does not meet the requirement, return False
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        # the node.val must be larget than all left node and less than upper bound
        left = self.helper(node.left, lower_bound, node.val)
        # the node.val must be smaller than all right node and larger than lower bound
        right = self.helper(node.right, node.val, upper_bound)
        return left and right