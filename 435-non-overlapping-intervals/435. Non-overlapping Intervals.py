class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        a=sorted(intervals,key=lambda x: x[1])
        end=float('-inf')
        count=0
        for s,e in a:
            if s>=end:
                end=e
            else:
                count+=1
        return count

            