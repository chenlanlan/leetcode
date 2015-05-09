#!/usr/bin/python

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

'''
设三个指针，temp。next记录进行连接的层的开始点，p记录当前层的上一层，pre记录上一个TreeNode的位置
'''
class Solution:
    # @param root, a tree link node
    # @return nothing    
    def connect(self, root):
        if root == None:
            return
        while root != None:
            temp = TreeLinkNode(0)
            p = root
            pre = temp
            while p != None:
                if p.left != None:
                    pre.next = p.left
                    pre = pre.next
                if p.right != None:
                    pre.next = p.right
                    pre = pre.next
                p = p.next              
            root = temp.next
        return
            
