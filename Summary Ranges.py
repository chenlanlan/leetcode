class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        n = len(nums)
        if n == 0:
            return res
        s = ''
        i = 0
        while i < n - 1:
            if s == '':
                s += str(nums[i])
                if nums[i + 1] - nums[i] > 1:
                    res.append(s)
                    s = ''
            else:
                if nums[i + 1] - nums[i] > 1:
                    s += '->' + str(nums[i])
                    res.append(s)
                    s = ''
            i += 1
            print(s,i)
        if i == n - 1:
            if s == '':
                res.append(str(nums[n - 1]))
            else:
                s += '->' + str(nums[i])
                res.append(s)
        return res

test = Solution()
print(test.summaryRanges([1, 2]))