class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = 0
        target = len(nums) - 1
        
        for i, j in enumerate(nums):
            if i > a:
                return False
            a = max(a, i + j)
            if a >= target:
                return True
                
        return a >= target