class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums)<2:
            return nums
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            
        return nums
        
        