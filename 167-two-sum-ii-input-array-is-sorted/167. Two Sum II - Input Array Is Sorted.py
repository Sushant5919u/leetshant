class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen={}
        for i,j in enumerate(numbers):
            if target - j in seen:
                return [seen[target-j]+1,i+1]
            else:
                seen[j]=i
        return []
        