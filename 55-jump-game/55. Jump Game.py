class Solution:
    def canJump(self, nums: List[int]) -> bool:
        limit=0
        for i in range(len(nums)):
            if i>limit:
                return False
            limit=max(limit,i+nums[i])
        return True