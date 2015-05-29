#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        ans = []
        n = len(nums)
        d = {}
        if n < 4:
            return ans
        nums.sort()
        for p in range(n):
            for q in range(p + 1, n):
                if nums[p] + nums[q] not in d:
                    d[nums[p] + nums[q]] = [(p, q)]
                else:
                    d[nums[p] + nums[q]].append((p, q))
        for i in range(n):
            for j in range(i + 1, n - 2):
                T = target - nums[i] - nums[j]
                if T in d:
                    for k in d[T]:
                        if k[0] > j and [nums[i], nums[j], nums[k[0]], nums[k[1]]] not in ans:
                            ans.append([nums[i], nums[j], nums[k[0]], nums[k[1]]])
            
        return ans

test = Solution()
print(test.fourSum([1, 0, -1, 0, -2, 2], 0))
