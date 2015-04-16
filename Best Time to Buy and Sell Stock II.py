#!/user/bin/python

def maxProfit2(self, prices):
    if len(prices) == 0:
        return 0
    lowest = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] >= prices[i - 1]:
            continue
        profit += prices[i - 1] - lowest
        lowest = prices[i]
    profit += prices[len(prices) - 1] - lowest
    return profit

self = 0
prices = [1, 2]
print(maxProfit2(self, prices))
