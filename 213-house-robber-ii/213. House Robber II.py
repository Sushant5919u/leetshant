class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base case: if there's only one house, just rob it
        if len(nums) == 1:
            return nums[0]
            
        # Helper function containing your original linear House Robber logic
        def rob_linear(houses: List[int]) -> int:
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
                
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
                
            return dp[-1]
        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))