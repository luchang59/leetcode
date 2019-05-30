# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):# List[int]) -> TreeNode:
        """
        use recursion, left subtree use the left part sublist, right subtree use the right part sublist.
        """

        if not nums: return None
        
        if len(nums) == 1: return TreeNode(nums[0])
        
        val = max(nums)
        index = nums.index(val)
        node = TreeNode(val)
        
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return node


        # iteration, not commend
        # if not nums:
        #     return None
        # stk = []
        # last = None
        # for num in nums:
        #     while stk and stk[-1].val < num:
        #         last = stk.pop()
        #     node = TreeNode(num)
        #     if stk:
        #         stk[-1].right = node 
        #     if last:
        #         node.left = last
        #     stk.append(node)
        #     last = None
        # return stk[0]