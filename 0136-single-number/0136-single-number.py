class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = True
                continue
            hash_map[num] = False
        
        for k, v in hash_map.items():
            if v:
                return k
            