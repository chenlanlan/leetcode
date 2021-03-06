#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        res = []
        if root == None:
            return res
        queue = []
        queue.append(root)
        array = []
        curLevel = 1
        nextLevel = 0
        while queue != []:
            cur = queue[0]
            del queue[0]
            array.append(cur.val)
            curLevel -= 1
            if cur.left:
                queue.append(cur.left)
                nextLevel += 1
            if cur.right:
                queue.append(cur.right)
                nextLevel += 1

            if curLevel == 0:
                res.append(array)
                array = []
                curLevel = nextLevel
                nextLevel = 0
        res.reverse()
        return res
                
