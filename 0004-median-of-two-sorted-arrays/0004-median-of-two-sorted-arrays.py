class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if (total_length) % 2 == 1:
            if len(nums1) == 0:
                return nums2[(len(nums2) // 2 )]
            elif len(nums2) == 0:
                return nums1[(len(nums1) // 2 )]
            a = (nums1+nums2)
            a.sort()
            return a[(total_length // 2)]
        
        if len(nums1) == 0:
            mid1 = len(nums2) // 2
            return sum(nums2[mid1 - 1: mid1 + 1]) / 2
        
        if len(nums2) == 0:
            mid2 = len(nums1) // 2
            return sum(nums1[mid2 - 1: mid2 + 1]) / 2
    

        # possible_nums = nums1[len(nums1) // 2 -1:len(nums1) // 2 + 1]
        # # if len(possible_nums) == 1:
        # #     for n in nums2:
        # #         if n <= possible_nums[0]:
        # #             possible_nums.append(possible_nums[0])
        # #             possible_nums[0] = n

        # # if possible_nums[1] < nums2[0]:
        # #     for i in range(len(nums2) // 2):
        # #         possible_nums[0] = possible_nums[1]
        # #         possible_nums[1] = nums2[i]
        # # else:
        # possible_nums2 = nums2[len(nums2) // 2 -1:len(nums2) // 2 + 1]
        a = nums1 + nums2
        a.sort()
        possible_nums = a[len(a) // 2 - 1: len(a) // 2 + 1]
        return sum(possible_nums) / 2
        #     # for n in possible_nums2:
        #         # if n >= possible_nums[1]:
        #         #     continue
        #         # elif n < possible_nums[1]:
        #         #     if possible_nums[0] < n:
        #         #         possible_nums[0] = n
        #         #     elif possible_nums[0] == n:
        #         #         possible_nums[1] = n
        # return (possible_nums[0] + possible_nums[1]) / 2