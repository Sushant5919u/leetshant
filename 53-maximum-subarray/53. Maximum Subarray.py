class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum2 = nums[0]
        sum1 = nums[0]

        for i in range(1, len(nums)):
            sum1 = max(nums[i], sum1 + nums[i])
            sum2 = max(sum2, sum1)

        return sum2
