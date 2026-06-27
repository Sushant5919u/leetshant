class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            b=0
            for j in nums:
                if i>j:
                    b+=1
            a.append(b)
        return a
        