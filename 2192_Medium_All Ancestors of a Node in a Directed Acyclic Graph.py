class Solution:
    def getAncestor(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = defaultdict(list)
        for edge in edges:
            m[edge[1]].append(edge[0])

        ret = [[] for _ in range(n)]

        for i in range(0, n):
            if m[i] == []:
                continue

            visited = set()
            q = deque(m[i])
            while q:
                current_node = q.popleft()
                if current_node in visited:
                    continue
                ret[i].append(current_node)
                for element in m[current_node]:  # add to queue
                    q.append(element)

        # sort ret
        for i in range(0, n):
            ret[i].sort()

        return ret
