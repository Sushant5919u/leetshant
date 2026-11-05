class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        def memo(n: int) -> int:
            if n == 0 or n == 1:
                return n
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = memo(n - 1) + memo(n - 2)
            return dp[n]
            
        return memo(n)