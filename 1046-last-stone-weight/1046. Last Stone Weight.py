import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        stones=[-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first!=second:
                heapq.heappush(stones, (first-second) * -1)
        return -stones[0] if stones else 0


        
        