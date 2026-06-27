class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=[]
        b=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j]:
                    a.append([i,j])
        return len(a)