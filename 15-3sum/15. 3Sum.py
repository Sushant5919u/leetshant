class Solution:
    def threeSum(self, A: list[int]) -> list[list[int]]:
        A.sort()
        c=[]
        for i in range(len(A)):
            if i > 0 and A[i] == A[i - 1]:
                continue
                
            left = i + 1
            right = len(A) - 1 
            b = A[i] * -1
            
            while left < right:
                if A[left] + A[right] == b:
                    c.append([A[i], A[left], A[right]])
                    left += 1
                    right -= 1
                    while left < right and A[left] == A[left - 1]:
                        left += 1
                elif A[left] + A[right] < b:
                    left += 1
                elif A[left] + A[right] > b:
                    right -= 1
        return c

                    
                