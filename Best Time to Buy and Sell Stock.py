#!/user/bin/python

def maxProfit(self, prices):
    if len(prices) == 0:
        return 0
    lowest = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
        elif prices[i] - lowest > profit:
            profit = prices[i] - lowest
    return profit

self = 0
prices = [5, 3, 1, 5, 2, 1]
print(maxProfit(self, prices))



