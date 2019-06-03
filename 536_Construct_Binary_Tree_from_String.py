# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    actually, this problem is a little bit difficult.
    use recursion to build the treenode, and if '(' appears after ')', it means there have right node.
    it use index to find the element, if s[i] is digital, build the TreeNode, if s[i] == '(' means subtree. 
    Therefore, recurse it. and use i += 1 to skip '(' and ')'
    """
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        root, _ = self.helper(s, 0)
        return root
    
    def helper(self, s, i):
        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()): # negative sign or digit
            i += 1
        node = TreeNode(int(s[start : i]))
        if i < len(s) and s[i] == '(':
            i += 1 # skip '('
            node.left, i = self.helper(s, i)
            i += 1 # skip ')'
        if i < len(s) and s[i] == '(': # still has '(', create right tree
            i += 1 # skip '('
            node.right, i = self.helper(s, i)
            i += 1 # skip ')'
        return node, i