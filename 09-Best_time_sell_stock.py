# Question link => https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Sliding Window (Two Pointers) Technique.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        while r != len(prices):
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                max_profit = max(max_profit,profit)
            else:
                l = r
            r += 1
        return max_profit 