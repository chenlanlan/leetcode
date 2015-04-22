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
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > profit:
                profit = prices[i] - min
        return profit

x = Solution()
print(x.maxProfit([5, 3, 1, 5, 2, 1]))



