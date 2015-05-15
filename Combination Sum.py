#!/usr/bin/python

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def __init__(self):
        self.result = []
    def combinationSum(self, candidates, target):
        solution = []
        candidates.sort()
        def getCombination(candidates, target, sum ,level):
            if sum > target:
                return
            if sum == target:
                self.result.append(solution[:])
                return
            else:
                for i in range(level, len(candidates)):
                    sum += candidates[i]
                    solution.append(candidates[i])
                    getCombination(candidates, target, sum, i)
                    solution.pop()
                    sum -= candidates[i]
        getCombination(candidates, target, 0, 0)
        return self.result

test = Solution()
print(test.combinationSum([8,7, 4, 3], 11))
        
        
            
