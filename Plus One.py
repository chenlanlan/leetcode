#!/usr/bin/python

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        ans = digits
        is_carry = True
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] == 9:
                ans[i] = 0
            else:
                ans[i] += 1
                is_carry = False
                break
        if is_carry:
            ans.insert(0, 1)
        return ans
        
x = Solution()
print(x.plusOne([9]))


