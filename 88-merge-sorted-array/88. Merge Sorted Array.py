class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in nums2:
            if 0 in nums1:
                nums1.remove(0)
            nums1.append(i)
        nums1.sort()
        