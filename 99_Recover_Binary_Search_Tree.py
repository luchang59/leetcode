# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# this question requirs a O(1) space, but following solution is O(n) space.
class Solution:
    def recoverTree(self, root):
        
        swapNodes = []

        def inorderTravere(node):
            prev, curr, stack = None, root, []

            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                if prev and prev.val >= curr.val:
                    swapNodes.append(prev)
                    swapNodes.append(curr)
                prev = curr
                curr = curr.right

        inorderTravere(root)
        first, second = swapNodes[0], swapNodes[-1]
        first.val, second.val = second.val, first.val

        # Morris Traversal
        first, second = None, None
        firstTime = True
        prev = TreeNode(float('-inf'))
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    temp.right = root #搭桥
                    root = root.left
                else:
                    temp.right = None # 拆桥
                    # visit root.val
                    if prev.val > root.val and firstTime:
                        first = prev
                        firstTime = False
                    if prev.val > root.val and not firstTime:
                        second = root
                    prev = root
                    root = root.right
            else:
                if prev.val > root.val and firstTime:
                    first = prev
                    firstTime = False
                if prev.val > root.val and not firstTime:
                    second = root
                prev = root
                root = root.right
        if first and second:
            first.val, second.val = second.val, first.val