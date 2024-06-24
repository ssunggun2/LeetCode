class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while 0 in nums1[m:]:
            nums1.pop()
        # for i in range(len(nums1) - 1, -1, -1):
        #     print(i)
        #     if nums1[i] == 0:
        #         nums1.pop()
        #     else:
        #         break
        nums1.extend(nums2)
        nums1.sort()