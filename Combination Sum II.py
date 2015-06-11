#!/usr/bin/python

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def __init__(self):
        self.result = []
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.combine(candidates, target, 0, 0, [])
        return self.result

    def combine(self, candidates, target, index, sum, temp):
        if sum > target :
            return
        if sum == target:
            if not temp in self.result:
                self.result.append(temp[:])
                return
        else:
            for i in range(index, len(candidates)):
                if i == index or candidates[i] != candidates[i - 1]:
                    sum += candidates[i]
                    temp.append(candidates[i])
                    self.combine(candidates, target, i + 1, sum, temp)
                    sum -= candidates[i]
                    temp.pop()

test = Solution()
print(test.combinationSum2([1, 2], 4))
        
        
            
