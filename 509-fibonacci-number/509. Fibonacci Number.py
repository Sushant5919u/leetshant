class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        prev=0
        prev2=1
        for i in range(2,n+1):
            prev,prev2=prev2,prev+prev2
        return prev2
        