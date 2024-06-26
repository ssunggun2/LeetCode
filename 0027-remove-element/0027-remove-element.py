class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        while val in nums:
            nums.remove(val)
            cnt += 1
        ans = len(nums)
        for i in range(cnt):
            nums.append('_')
        return ans
            