#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        res = 0
        for i in range(n):
            count = 0
            temp = nums[i]
            j = i + 2
            length = n - res
            while j < length and nums[j] == temp:
                j += 1
                count += 1
                res += 1
            if count != 0:
                for k in range(j, n):
                    nums[k - count] = nums[k]
        n -= res
        return n

    def removeDuplicates2(self, nums):
        n = len(nums)
        i = 2
        count = 2
        c = 0
        if n == 0 or n == 1:
            return n
        while i < n:
            if nums[count - 2] != nums[i]:
                nums[count] = nums[i]
                count += 1
            else:
                c += 1
            i += 1
        return n - c

test = Solution()
print(test.removeDuplicates([1, 1, 1, 1]))
print(test.removeDuplicates2([1, 1, 1, 2, 2, 2, 3, 3]))
            
            
