from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max_product = prod(nums) 
        if max_product != 0 :
            return [max_product // n for n in nums]
        result = []
        for index, n in enumerate(nums):
            tmp_nums = nums[:]
            if n == 0:
                tmp_nums.pop(index)
                result.append(prod(tmp_nums))
            else:
                result.append(0)
        return result

