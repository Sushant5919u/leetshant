class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]
        n = len(A)
        memo = {}
        
        def dp(left, right):
            if left + 1 == right:
                return 0
                
            if (left, right) in memo:
                return memo[(left, right)]
                
            max_coins = 0
            for i in range(left + 1, right):
                coins = A[left] * A[i] * A[right] + dp(left, i) + dp(i, right)
                max_coins = max(max_coins, coins)
                
            memo[(left, right)] = max_coins
            return max_coins
        return dp(0, n - 1)