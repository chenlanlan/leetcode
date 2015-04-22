#!/user/bin/python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        length = len(num)
        for i in range (1, length):
            if num[i] < num[i-1]:
                return i - 1
        return length - 1

x = Solution()
print (x.findPeakElement([1, 2, 3, 1, 1]))

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement2(self, num):
        left = 0
        right = len(num) - 1
        while left < right:   #left <= mid < right
            mid = (left + right) // 2
            if num[mid] < num[mid + 1] and mid  < len(num) - 1:
                left = mid + 1
            else:
                right = mid
        return left

    
    
