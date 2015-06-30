class Solution:
    # @param {integer} n
    # @return {integer[]}
    def __init__(self):
        self.res = []
    def grayCode(self, n):
        if n == 0:
            self.res.append(0)
            return self.res
        temp = self.grayCode(n - 1)
        addNumber = 1 << (n - 1)
        for i in range(len(temp) - 1, -1, -1):
            self.res.append(addNumber + temp[i])
        return self.res

test = Solution()
print(test.grayCode(3))