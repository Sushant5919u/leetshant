class Solution:
    def merge(self, intervals: List[List[int]])-> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        
        for i, j in intervals[1:]:
            start2, end2 = ans[-1]
            if i <= end2:
                ans[-1][1] = max(j, end2)
            else:
                ans.append([i, j])
                
        return ans