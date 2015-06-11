#!/usr/bin/python

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def __init__(self):
        self.result = []

    def combine(self, candidates, target, index, sum, temp):
        if sum > target:
            return 
        if sum == target:
            self.result.append(temp[:])
            return
        else:
            for i in range(index, len(candidates)):
                sum += candidates[i]
                temp.append(candidates[i])
                self.combine(candidates, target, i, sum, temp)
                sum -= candidates[i]
                temp.pop()
            return

    def combinationSum(self, candidates, target):
        n = len(candidates)
        sum = 0
        candidates.sort()
        self.combine(candidates, target, 0, sum, [])
        return self.result

test = Solution()
print(test.combinationSum([8,7, 4, 3], 11))
        
        
            
