#!/usr/bin/python

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        length = len(nums)
        step = k % length
        def reverse(i, j, Array):
            while i < j:
                temp = Array[i]
                Array[i] = Array[j]
                Array[j] = temp
                i += 1
                j -= 1
            return Array
        reverse(0, length - 1, nums)
        return nums

x = Solution()
print (x.rotate([1], 0))
            
            
