class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        tag = False
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 0 :
                tag = False
                continue
            else:
                if ((arr[i] + arr[i + 1]) % 2 == 0) and ((arr[i] + arr[i + 2]) % 2 == 0):
                    return True
        return False
            