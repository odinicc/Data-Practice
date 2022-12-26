import math

#def maxProfit(self, prices):
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit

    while


prices = [7,6,4,3,1]


print(maxProfit(prices ))

