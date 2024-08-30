class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        neighbors = defaultdict(set)

        # Construct the graph by connecting stones sharing the same row or column
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                point1, point2 = stones[i], stones[j]
                if point1[0] == point2[0] or point1[1] == point2[1]:
                    neighbors[i].add(j)
                    neighbors[j].add(i)

        checked = [False] * len(stones)

        def bfs(start):
            queue = deque([start])
            checked[start] = True
            while queue:
                node = queue.popleft()
                for neighbor in neighbors[node]:
                    if not checked[neighbor]:
                        checked[neighbor] = True
                        queue.append(neighbor)

        # Count connected components
        num_components = 0
        for i in range(len(stones)):
            if not checked[i]:
                bfs(i)
                num_components += 1

        # Maximum stones that can be removed is total stones - number of connected components
        return len(stones) - num_components
