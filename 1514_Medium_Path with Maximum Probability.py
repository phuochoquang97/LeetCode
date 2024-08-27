class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = defaultdict(list)
        for (n0, n1), p in zip(edges, succProb):
            graph[n0].append((n1, p))
            graph[n1].append((n0, p))

        # simulate min-heap in python by converting prob to negative
        max_heap = [(-1, start_node)]
        prob = [0] * n
        prob[start_node] = 1

        while max_heap:
            # find the next node
            current_prob, current_node = heapq.heappop(max_heap)
            # convert back to positive
            current_prob = -current_prob

            if current_node == end_node:
                return current_prob

            for nb, p in graph[current_node]:
                new_prob = current_prob * p
                # update prob of nb
                if new_prob > prob[nb]:
                    prob[nb] = new_prob
                    heapq.heappush(max_heap, (-new_prob, nb))

        return 0
