class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=[]
        b=0
        for i in nums:
            if i != val:
                a.append(i)
        for i in range(len(a)):
            nums[i] = a[i]
        return len(a)