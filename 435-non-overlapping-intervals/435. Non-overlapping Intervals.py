class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        a=sorted(intervals,key=lambda x: x[1] )
        count = 0
        last_end = float("-inf")

        for s, e in a:
            if s >= last_end:
                
                last_end = e
            else:
                count += 1

        return count
            