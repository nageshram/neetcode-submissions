class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        profit=0
        for i in range(l):
            buy=prices[i]
            for j in range(i+1,l):
                sell=prices[j]
                profit=max(profit,sell-buy)
        return profit