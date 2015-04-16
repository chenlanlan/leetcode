#!/user/bin/python

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

self = 0
prices = [5, 3, 1, 5, 2, 1]
print(maxProfit(self, prices))



