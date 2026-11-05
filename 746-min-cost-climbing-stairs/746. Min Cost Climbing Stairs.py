class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        res = [0] * len(cost)
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2, len(cost)):
            res[i] = min(res[i-1], res[i-2]) + cost[i]


        return min(res[-2], res[-1])
            
        