#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        def merge(A, p, q, r):
            n1 = q - p + 1
            n2 = r - q
            L = A[p : q + 1]
            R = A[q + 1 : r + 1]
            i = 0
            j = 0
            for k in range(p, r + 1):
                if i < n1 and j < n2:
                    if L[i] < R[j]:
                        A[k] = L[i]
                        i += 1
                    else:
                        A[k] = R[j]
                        j += 1
                elif i == n1:
                    A[k] = R[j]
                    j += 1
                elif j == n2:
                    A[k] = L[i]
                    i += 1
            return A
        def sort(A, p, r):
            if p < r:
                q = (p + r) // 2
                sort(A, p, q)
                sort(A, q + 1, r)
                merge(A, p, q, r)
            return A
        nums = sort(nums, 0, len(nums) - 1)
        max = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                temp += 1
            elif nums[i] == nums[i - 1]:
                temp = temp
            elif temp > max:
                max = temp
                temp = 1
            else:
                temp = 1
        if temp > max:
            max = temp
        return max
                
        

test = Solution()
print(test.longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))
            
            
