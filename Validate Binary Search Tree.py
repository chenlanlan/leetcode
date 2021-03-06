#!/usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root): #最大最小值法
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        def ValidBST(root, min, max):
            if root == None:
                return True
            if root.val <= min or root.val >= max:
                return False
            return ValidBST(root.left, min, root.val) and ValidBST(root.right, root.val, max)
        return ValidBST(root, INT_MIN, INT_MAX)

    
    
    def inOrderTraversal(self, root, List):#中序遍历法
        if root == None:
            return
        self.inOrderTraversal(root.left, List)
        List.append(root.val)
        self.inOrderTraversal(root.right, List)
    
    def isValidBST(self, root):
        if root == None or root.left == None and root.right == None:
            return True
        List = []
        self.inOrderTraversal(root, List)
        for i in range(1, len(List)):
            if List[i] <= List[i - 1]:
                return False
        return True

