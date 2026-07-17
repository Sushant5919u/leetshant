class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        left_sum = 0
        min_diff = float('inf')
        ans_idx = -1
        
        for i in range(n):
            # Update left sum and calculate right sum dynamically
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            
            # Calculate left average
            left_avg = left_sum // (i + 1)
            
            # Calculate right average (handle the last element where right side is empty)
            if n - i - 1 > 0:
                right_avg = right_sum // (n - i - 1)
            else:
                right_avg = 0
                
            # Take the absolute difference properly
            diff = abs(left_avg - right_avg)
            
            # Track the strict minimum to ensure the smallest index wins in ties
            if diff < min_diff:
                min_diff = diff
                ans_idx = i
                
        return ans_idx