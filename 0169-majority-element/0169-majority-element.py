class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
                continue
            hash_map[num] += 1
            if hash_map[num] >= int(len(nums) / 2) + 1:
                return num           
