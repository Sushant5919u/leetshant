class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in points:
            heapq.heappush(heap,((i[0]**2 + i[1]**2),i))
        ans = []

        for i in range(k):
            distance, point = heapq.heappop(heap)
            ans.append(point)

        return ans