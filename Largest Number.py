#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def compare(self, num1, num2):
            if len(num1) != len(num2):
                num1, num2 = num1 + num2, num2 + num1
            if num1 > num2:
                return 1
            elif num1 == num2:
                return 0
            else:
                return -1

    def findlow(self, A, low, high):
        key = A[low]
        while low < high:
            while self.compare(A[high], key) != -1 and low < high:
                high -= 1
            A[low], A[high] = A[high], A[low]
            while self.compare(A[low], key) != 1 and low < high:
                low += 1
            A[low], A[high] = A[high], A[low]
        return low
            
    def sort(self, A, low, high):
        if low < high:
            p = self.findlow(A, low, high)
            self.sort(A, low, p - 1)
            self.sort(A, p + 1, high)
        return A
        
    def largestNumber(self, nums):
        n = len(nums)
        if n == 0:
            return None
        dict = {}
        for num in nums:
            num = str(num)
            if not num in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        keys = list(dict.keys())
        low = 0
        high = len(keys) - 1
        keys = self.sort(keys, low, high)
        keys.reverse()
        result = ''
        for k in keys:
            result = result + str(k) * dict[k]

        result = result.lstrip('0')
        if len(result) == 0:
            return '0'
        else:
            return result

test = Solution()
print(test.largestNumber([1, 2, 1]))
            
