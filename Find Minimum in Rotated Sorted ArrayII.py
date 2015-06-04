#!/usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        left = 0
        right = n - 1
        while left < right:
            if num[left] < num[right]:
                return num[left]
            mid = left + (right - left) // 2
            if num[left] == num[mid]:
                if left + 1 == right:
                    if num[left] >= num[right]:
                        left = right
                        break
                else:
                    left += 1
            
            elif num[mid] > num[left]:
                left = mid
            else:
                right = mid
        return num[left]
    def findMin2(self, num):
        left = 0
        right = len(num) - 1
        while left < right:
            if num[left] < num[right]:
                return num[left]
            mid = (left + right) // 2
            if num[mid] == num[left]:
                if left + 1 == right:
                    if num[left] >= num[right]:
                        left = right
                        break
                else:
                    left += 1
            if num[left] < num[mid]:
                left = mid
            else:
                right = mid
            print(left, right)
        return num[left]

x = Solution()
print(x.findMin2([3, 3, 1]))
