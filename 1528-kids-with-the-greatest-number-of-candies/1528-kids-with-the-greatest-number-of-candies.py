class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for kid in candies:
            ans.append(kid + extraCandies >= max_candies)
        return ans