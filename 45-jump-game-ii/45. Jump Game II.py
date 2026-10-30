class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest=0
        jump=0
        end=0
        for i in range(len(nums)-1):
            if len(nums)<1:
                return 0
            farthest=max(farthest,i+nums[i])
            if end==i:
                jump+=1
                end=farthest
        return jump
            


            