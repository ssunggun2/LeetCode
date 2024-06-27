class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u = edges[0][0]
        return u if u in edges[1] else edges[0][1]