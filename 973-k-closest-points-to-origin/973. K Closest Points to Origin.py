class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for point in points:
            distance = -(point[0]**2 + point[1]**2)

            heapq.heappush(heap, (distance, point))

            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            distance,point=heapq.heappop(heap)
            ans.append(point)
        return ans