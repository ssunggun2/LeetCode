class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if len(nums) - 3 + i > len(nums):
                break
            ans.append(nums[i: len(nums) - 3 + i ])
        a = []
        for i in ans:
            a.append(i[-1] - i[0])
        return min(a)

        