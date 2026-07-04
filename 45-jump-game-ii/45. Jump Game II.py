class Solution:
    def jump(self, nums: List[int]) -> int:
        b = len(nums) - 1
        if b < 1:
            return 0
        
        a = 0  
        c = 0  
        d = 0 
        
        for i in range(b):
            j = nums[i]
            a = max(a, i + j)
            if i == d:
                c += 1              
                d = a 
                if d >= b:
                    break
                    
        return c