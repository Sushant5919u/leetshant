class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        count=i=j=0
        while i<len(g) and j <len(s):
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count
       