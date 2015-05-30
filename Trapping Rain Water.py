#!/usr/bin/python

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        res = 0
        leftMax = [0 for i in range(n)]
        rightMax = [0 for i in range(n)]
        for i in range(n):
            if i == 0:
                leftMax[i] = max(height[i], 0)
            else:
                leftMax[i] = max(height[i], leftMax[i - 1])
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                rightMax[i] = max(height[i], 0)
            else:
                rightMax[i] = max(height[i], rightMax[i + 1])
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

    def trap2(self, height):
        n = len(height)
        left = 0
        right = n - 1
        secHight = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                secHight = max(secHight, height[left])
                ans += secHight - height[left]
                left += 1
            else:
                secHight = max(secHight, height[right])
                ans += secHight - height[right]
                right -= 1
        return ans

test = Solution()
print(test.trap2([2,1,0,1,3]))
        
