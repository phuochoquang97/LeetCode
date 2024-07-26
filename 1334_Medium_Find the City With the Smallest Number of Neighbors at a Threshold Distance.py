class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # for each city, find how many cities can be reached from current city
        # with d(current, city-i) <= distanceThreshold

        # for each city, dijikstra(current, city-i), then count how many distance != INF
        # sort based on nb of city -> city value
        # time complexity O(n^2)

        # store the neighbors of each node node: (neighbor, weight)
        mapping = defaultdict(list)
        for node, neighbor, weight in edges:
            mapping[node].append([neighbor, weight])
            mapping[neighbor].append([node, weight])

        def dijkstra(node):
            distance_store = [float("inf")] * n
            visited = [False] * n
            distance_store[node] = 0
            q = deque()
            q.append(node)
            while q:
                current_node = q.popleft()
                visited[current_node] = True
                visited[current_node] = True
                for neighbor, weight in mapping[current_node]:
                    if (distance_store[current_node] + weight) <= distance_store[neighbor]:
                        distance_store[neighbor] = distance_store[current_node] + weight
                        q.append(neighbor)

            count = 0
            for d in distance_store:
                if (d <= distanceThreshold) and (d != 0):
                    count += 1

            return count

        # process each node
        ret_store = []
        for node in range(n):
            count = dijkstra(node)
            ret_store.append((node, count))

        ret_store_sorted = sorted(ret_store, key=lambda x: (x[1], -x[0]))

        return ret_store_sorted[0][0]
