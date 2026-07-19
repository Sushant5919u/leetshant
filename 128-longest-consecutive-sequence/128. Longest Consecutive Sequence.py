class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        b=0
        for i in a:
            if (i-1) not in a:
                c=i
                s=1
                while (c+1) in a:
                    s+=1
                    c+=1
                b=max(b,s)
        return b