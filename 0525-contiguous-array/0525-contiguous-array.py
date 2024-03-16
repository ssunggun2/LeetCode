
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_dict = {0 : -1}
        count = 0
        max_length = 0
        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in diff_dict:
                max_length = max(max_length , index - diff_dict[count])
            else:
                diff_dict[count] = index
        return max_length
            

        