class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        while i < len(intervals)-1:
            a,b=intervals[i]
            c,d=intervals[i+1]
            if b>=c:
                intervals[i+1]=[a,max(b,d)]
                del intervals[i]
            else:
                i+=1
        return intervals
                    

        