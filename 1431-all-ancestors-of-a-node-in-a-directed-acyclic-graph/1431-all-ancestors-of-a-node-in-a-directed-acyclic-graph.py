class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edge_dict = defaultdict(list)
        for edge in edges:
            f = edge[0]
            t = edge[1]
            edge_dict[t].append(f)
        ancestors = [[] for _ in range(n)]
        def dfs(node):
            if not ancestors[node]:
                for ancestor in edge_dict[node]:
                    ancestors[node].append(ancestor)
                    ancestors[node].extend(dfs(ancestor))
                ancestors[node] = list(set(ancestors[node]))
                ancestors[node].sort()
            return ancestors[node]
        
        for i in range(n):
            dfs(i)
        
        return ancestors