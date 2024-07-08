class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        max_sums = sums
        if len(nums) == k:
            return sum(nums) / k
        for i in range(1, len(nums) - k + 1):
            sums = sums + nums[i + k - 1] - nums[i - 1]   
            if sums > max_sums :
                max_sums = sums
        return max_sums / k