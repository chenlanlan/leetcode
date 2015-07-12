# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q: return
        if root and self.isFather(root, p) and self.isFather(root, q):
            self.ans = root
            self.lowestCommonAncestor(root.left, p, q)
            self.lowestCommonAncestor(root.right, p, q)
        return self.ans
    
    def isFather(self, n1, n2):
        if not n1: return False
        if n1 == n2 : return True
        
        return self.isFather(n1.left, n2) or self.isFather(n1.right, n2)