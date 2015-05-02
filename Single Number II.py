#!/user/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = ones^num & ~twos
            twos = twos^num & ~ones
        return ones

x = Solution()
print(x.singleNumber([1, 2, 3, 4, 1, 2, 3, 1, 2, 3]))
