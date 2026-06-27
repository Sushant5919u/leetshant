class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        mapp = {}
        res = []
        for i in range(len(temp)):
            if temp[i] not in mapp:
                mapp[temp[i]] = i
        for i in range(len(nums)):
            res.append(mapp[nums[i]])
        return res