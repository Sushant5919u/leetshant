class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        zero_count = 0
        b = []
        
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                a *= i
                
        for i in nums:
            if zero_count > 1:
                b.append(0)
            elif zero_count == 1:
                if i == 0:
                    b.append(int(a))
                else:
                    b.append(0)
            else:
                b.append(int(a / i))
                
        return b