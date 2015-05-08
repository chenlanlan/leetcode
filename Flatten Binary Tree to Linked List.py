#!/usr/bin/python

 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        self.printTree(root)
        if root == None:
            return
        left = root.left
        right = root.right
        if root.left != None:
            root.right = left
            root.left = None
            leftside = left
            while leftside.right != None:
                leftside = leftside.right
            leftside.right = right
        self.flatten(root.right)

    def printTree(self, node):
        if node == None:
            return
        print(node.val)
        print('--')
        self.printTree(node.left)
        self.printTree(node.right)

            
    
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
test = Solution()
#test.flatten(node1)
test.printTree(node1)
