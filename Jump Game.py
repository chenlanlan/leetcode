#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        i = 0
        n = len(nums)
        if nums[0] == 0:
            if n == 1:
                return True
            else:
                return False
        if not 0 in nums:
            return True
        def move(nums, pre, cur):
            if cur >= n - 1:
                return True
            if nums[cur] == 0:
                a = 1
                while nums[cur] < a and cur - 1 > pre:
                    cur -= 1
                    a += 1
                if cur - 1 < pre:
                    return False
            return move(nums, cur, cur + nums[cur])  
        return move(nums, -1, 0)

    def canJump2(self, nums):
        if len(nums) == 0:
            return False
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True

test = Solution()
print(test.canJump2([2, 1, 0, 0, 0]))
