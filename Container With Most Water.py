#!/usr/bin/python

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        n = len(height)
        sum = min(height[0], height[1])
        for i in range(n):
            for j in range(i + 1, n):
                if (j - i) * min(height[i], height[j]) > sum:
                    sum = (j - i) * min(height[i], height[j])
        return sum

    def maxArea2(self, height):
        start = 0
        end = len(height) - 1
        sum = 0
        while start < end:
            water = (end - start) * min(height[start], height[end])
            if water > sum:
                sum = water
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return sum

test = Solution()
print(test.maxArea2([2, 3, 3, 2, 8]))
                 
