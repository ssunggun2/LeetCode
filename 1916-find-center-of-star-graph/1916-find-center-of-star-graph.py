class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i, edge in enumerate(edges):
            if  i == 0:
                u = edge[0]
                v = edge[1]
                continue
            return u if u in edge else v