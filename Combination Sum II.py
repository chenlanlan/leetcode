#!/usr/bin/python

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def __init__(self):
        self.result = []
    def combinationSum2(self, candidates, target):
        solution = []
        candidates.sort()
        def getCombination(candidates, target, sum ,level):
            if sum == target:
                if not solution in self.result:
                    self.result.append(solution[:])
                return
            else:
                for i in range(level, len(candidates)):
                    if sum > target:
                        break
                    if i == level or candidates[i] != candidates[i - 1]:
                        sum += candidates[i]
                        solution.append(candidates[i])
                        getCombination(candidates, target, sum, i + 1)
                        solution.pop()
                        sum -= candidates[i]
        getCombination(candidates, target, 0, 0)
        return self.result

test = Solution()
print(test.combinationSum2([13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19], 25))
        
        
            
