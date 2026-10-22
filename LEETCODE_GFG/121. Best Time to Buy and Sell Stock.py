from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        diff = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i] 
                maxi = max(diff, maxi)
        return maxi

class Solution:
    def maxProfitOptimal(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if (prices[i]- min_price) > max_profit:
                max_profit = prices[i] -min_price
        return max_profit
