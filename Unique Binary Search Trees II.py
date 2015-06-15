#!/usr/bin/python


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        if n == 0:
            return [[]]
        return self.create(1, n)
    
    def create(self, start, end):
        results = []
        if start > end:
            return results
        k = start
        while k <= end:
            left = self.create(start, k - 1)
            right = self.create(k + 1, end)
            if left == [] and right == []:
                root = TreeNode(k)
                root.left = None
                root.right = None
                results.append(root)
            elif left == []:
                for i in range(len(right)):
                    root = TreeNode(k)
                    root.left = None
                    root.right = right[i]
                    results.append(root)
            elif right == []:
                for i in range(len(left)):
                    root = TreeNode(k)
                    root.left = left[i]
                    root.right = None
                    results.append(root)
            else:
                for i in range(len(left)):
                    for j in range(len(right)):
                        root = TreeNode(k)
                        root.left = left[i]
                        root.right = right[j]
                        results.append(root)
            k += 1
        
        return results


