class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        res = [0] * len(cost)
        for i in range( len(cost)):
            res[i] = min(res[i-1], res[i-2]) + cost[i]


        return min(res[-2], res[-1])
            
        