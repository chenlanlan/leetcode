#!/usr/bin/python

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        solution = []
        result = []
        sum = 0
        def combine(k, n, sum, level):
            if len(solution) > k:
                return
            if sum == n and len(solution) == k:
                result.append(solution[:])
                return
            else:
                for i in range(level, 10):
                    solution.append(i)
                    sum += i
                    combine(k, n, sum, i + 1)
                    solution.pop()
                    sum -= i
        combine(k, n, sum, 1)
        return result

test = Solution()
print(test.combinationSum3(3, 9))
