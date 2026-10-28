class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=set()
        for i in nums1:
            if i in nums2 and i not in a:
                a.add(i)
        return list(a)
        