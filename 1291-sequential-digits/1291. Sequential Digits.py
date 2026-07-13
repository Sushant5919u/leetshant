class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []
        
        for length in range(2, 10):
           
            for start in range(10 - length):
                num = int(sample[start : start + length])
            
                if low <= num <= high:
                    result.append(num)
                    
        return result