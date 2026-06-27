class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        profit = 0

        for i in prices:
            if i < mn:
                mn = i
            elif i - mn > profit:
                profit = i - mn

        return profit
