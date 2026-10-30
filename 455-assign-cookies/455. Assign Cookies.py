class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        a=0
        g.sort()
        s.sort()
        i=0
        j=0
        while i < (len(g)) and j < (len(s)):
                if s[j]>=g[i]:
                    a+=1
                    i+=1
                    j+=1
                elif s[j]<g[i]:
                    j+=1
        return a
        