class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=float('inf')
        b=0
        for i in prices:
            if i<a:
                a=i
            if i-a>b:
                b=i-a
        return b
