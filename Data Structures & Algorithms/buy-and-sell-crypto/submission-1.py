class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 100000000000000000
        for x in range(len(prices)):
            low = min(low, prices[x])
            temp = prices[x] - low
            profit =  max(profit, temp)
        return profit