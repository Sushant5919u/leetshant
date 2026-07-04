class Solution:
    def jump(self, nums: List[int]) -> int:
        b = len(nums) - 1
        if b < 1:
            return 0
        
        a = 0  # max_reachable
        c = 0  # jumps counter
        current_end = 0  # The end of the current jump's range
        
        # We loop up to b (len(nums) - 1) because we don't need to jump if we are already at the last element
        for i in range(b):
            j = nums[i]
            a = max(a, i + j)
            
            # If we reached the furthest point possible for the current jump
            if i == current_end:
                c += 1               # We must make another jump
                current_end = a      # Our new window extends to the maximum reachable point
                
                # If our new window can already touch or clear the end, we can stop early
                if current_end >= b:
                    break
                    
        return c