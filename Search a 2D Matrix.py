#!/usr/bin/python
#use binary search twice.
#First find the row index of the row to which the target might belong
#Then use binary search in the row to find the target

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def binarySearch(self, A, left, right, key):
        if A == []:
            return False
        while left < right:
            mid = (left + right) // 2
            if A[mid] == key:
                return True
            elif A[mid] < key:
                left = mid + 1
            elif A[mid] > key:
                right = mid
        return False
    
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        left = 0
        right = n
        rowIndex = -1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif left + 1 == right:
                rowIndex = left
                break
            elif matrix[mid][0] < target:
                left = mid
            elif matrix[mid][0] > target:
                right = mid
        print (rowIndex)
        if rowIndex != -1:
            return self.binarySearch(matrix[rowIndex], 0, len(matrix[rowIndex]), target)
        return False

test = Solution()
print(test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))


    
