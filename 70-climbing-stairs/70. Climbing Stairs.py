class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3 and n>=0:
            return n
        prev=1
        prev2=2
        for i in range(2,n):
            prev,prev2=prev2,prev+prev2
        return prev2

        

        