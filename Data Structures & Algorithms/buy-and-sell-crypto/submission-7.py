class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        for i in range(len(prices)):
            minimum = min(prices[i], minimum)
            if prices[i] > minimum:
                profit = max(profit, prices[i]-minimum)
        return profit
