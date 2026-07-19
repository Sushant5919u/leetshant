class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b={}
        for i in strs:
            s=''.join(sorted(i))
            if s in b:
                b[s].append(i)
            else:
                b[s]=[i]
        return list(b.values())