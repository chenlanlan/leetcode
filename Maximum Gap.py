#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findlow(self, A, low, high):
        key = A[low]
        while low < high:
            while A[high] >= key and low < high:
                high -= 1
            A[low], A[high] = A[high], A[low]          
            while A[low] <= key and low < high:
                low += 1
            A[low], A[high] = A[high], A[low]  
        return low
    def Sort(self, A, low, high):
        if low < high:
            P = self.findlow(A, low, high)
            self.Sort(A, low, P - 1)
            self.Sort(A, P + 1, high)
        return A
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums = self.Sort(nums, 0, len(nums) - 1)
        gap = nums[1] - nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i + 1] - nums[i] > gap:
                gap = nums[i + 1] - nums[i]
        return gap
        
A = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
x = Solution()
print(x.maximumGap(A))

