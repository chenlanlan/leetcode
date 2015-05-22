#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def __init__(self):
        self.ansList = []
        self.result = []
        
    def sub(self, nums, idx, n, k):
        result = []
        if idx == n:
            temp = []
            result.append(temp)
        else:
            vec = self.sub(nums, idx + 1, n, k)
            a = nums[idx]
            for i in range(len(vec)):
                v = vec[i]
                if len(v) == k:
                    self.ansList.append(v[:])
                else:
                    result.append(v[:])
                v.append(a)
                v.sort()
                if len(v) == k:
                    self.ansList.append(v[:])
                else:
                    result.append(v[:])
        return result
    
    def combine(self, n, k):
        result = []
        path = []
        nums = [i + 1 for i in range(n)]
        self.sub(nums, 0, len(nums), k)
        return self.ansList
        
# solution 2
    def combine2(self, n, k):
        path = []
        self.dfs(n, k, 1, 0, path)
        return self.result

    def dfs(self, n, k, start, cur, path):
        if cur == k:
            self.result.append(path[:])
        for i in range(start, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, cur + 1, path)
            path.pop()
            

test = Solution()
print(test.combine(3, 2))
print(test.combine2(3, 2))
