class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        if len(nums) <= 3:
            return sum(nums)

        closest_sum = float('inf')
        min_diff = float('inf')

        # O(N2)
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < min_diff:
                    min_diff = abs(current_sum - target)
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return  closest_sum


        # O(N3)
        # min_diff = float(inf)
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1 ):
        #         for k in range(j + 1 ,len(nums)):
        #             three_sum = nums[i] + nums[j] + nums[k]
        #             if three_sum == target:
        #                 return three_sum
        #             elif abs(three_sum - target) < min_diff :
        #                 min_diff = abs(target - three_sum)
        #                 result = three_sum
        # return result