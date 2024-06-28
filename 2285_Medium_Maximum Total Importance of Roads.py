class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        m = defaultdict(int)
        for road in roads:
            m[road[0]] += 1
            m[road[1]] += 1

        sorted_cities = sorted(m.values(), reverse=True)

        max_importance = 0
        for i in range(len(sorted_cities)):
            max_importance += sorted_cities[i] * n
            n -= 1

        return max_importance
