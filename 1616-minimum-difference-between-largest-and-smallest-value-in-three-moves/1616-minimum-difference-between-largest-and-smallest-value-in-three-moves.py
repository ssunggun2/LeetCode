from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        
        # 네 가지 경우의 차이를 계산
        case1 = nums[-1] - nums[3]      # 처음 세 개 제거
        case2 = nums[-2] - nums[2]      # 처음 두 개와 마지막 하나 제거
        case3 = nums[-3] - nums[1]      # 처음 하나와 마지막 두 개 제거
        case4 = nums[-4] - nums[0]      # 마지막 세 개 제거
        
        # 최소 차이를 반환
        return min(case1, case2, case3, case4)
