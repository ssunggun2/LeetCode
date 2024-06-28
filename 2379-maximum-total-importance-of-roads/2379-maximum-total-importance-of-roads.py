class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance_dict = {}
        for road in roads:
            for point in road:
                if not importance_dict.get(point):
                    importance_dict[point] = 1
                else:
                    importance_dict[point] += 1
        sorted_dict = sorted(importance_dict, key = lambda x: importance_dict[x], reverse = True)
        re_assign_dict = {}
        for key in sorted_dict:
            re_assign_dict[key] = n
            n -= 1
        total_importance = 0
        for road in roads:
            for point in road:
                total_importance += re_assign_dict[point]
        return total_importance