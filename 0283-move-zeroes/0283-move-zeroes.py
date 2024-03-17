class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        modi_nums = nums[:]
        for num in modi_nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)