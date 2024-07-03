class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        ans = []

        for i in range(n):
            if n - 3 + i > n:
                break
            ans.append(nums[i: n - 3 + i ])
        a = []
        for i in ans:
            a.append(i[-1] - i[0])
        return min(a)

        