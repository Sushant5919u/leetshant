class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

          s = ''.join(sorted(word))
          if s in groups:
            groups[s].append(word)
          else:
            groups[s]=[word]

        return list(groups.values())