class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(len(nums)):
            a=0
            for j in range(i+1):
                a+=nums[j]
            b.append(a)
        return b
    