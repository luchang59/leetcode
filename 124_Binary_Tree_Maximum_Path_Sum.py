# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # the core of this question is to maintain the maxValue, the helper function is made for it as well.
        self.maxValue = float('-inf')
        self.helper(root)
        return self.maxValue

    def helper(self, root):
        """
        This helper function is designed to consider the sum include both side or just one side.
        """
        if not root: return 0
        
        # get the left path and right path value, if the value less than 0, don't add it into the path
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        # sum the root node, left value and right value, make a new path value
        pathLeftRight = sum(root.val, left, right)
        # compare and update the current maxValue and the new path value
        self.maxValue = max(self.maxValue, pathLeftRight)
        # this return is for the recursion (for left value and right value)
        return root.val + max(left, right)