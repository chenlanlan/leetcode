#!/user/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        ans = max(nums)
        if len(nums) == 1:
            return nums[0]
        ans_positive = [0 for i in range(len(nums))]
        ans_negative = [0 for i in range(len(nums))]
        if nums[0] < 0:
            ans_negative[0] = nums[0]
        elif nums[0] > 0:
            ans_positive[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                ans_positive[i] = max(ans_positive[i - 1] * nums[i], nums[i])
                ans_negative[i] = ans_negative[i - 1] * nums[i]
            elif nums[i] < 0:
                ans_positive[i] = ans_negative[i - 1] * nums[i]
                ans_negative[i] = min(ans_positive[i - 1] * nums[i], nums[i])
            if ans_positive[i] > ans:
                ans = ans_positive[i]
        return ans

test = Solution()
print(test.maxProduct([2, -5, 3, 6]))
