class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        prefix = {0:1}
        for i in nums:
            cur += i
            diff = cur - k
            res += prefix.get(diff,0)
            prefix[cur] = 1 + prefix.get(cur,0)
        return res
        