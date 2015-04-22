#!/user/bin/python

class Solution:
    # @param prices, an integer[]
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                continue
            profit += prices[i - 1] - min
            min = prices[i]
        profit += prices[len(prices) - 1] - min
        return profit

x = Solution()
print(x.maxProfit([1, 2, 4]))
