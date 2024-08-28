class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # bfs grid2, check if match with grid1 then count += 1 else break
        m = len(grid1)
        n = len(grid1[0])

        count = 0
        visited = [[False] * n for _ in range(m)]

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        def bfs(x, y):
            check = True
            q = deque()
            q.append((x, y))
            while q:
                u_x, u_y = q.popleft()
                visited[u_x][u_y] = True
                if grid1[u_x][u_y] != 1:
                    check = False
                for i in range(4):
                    xi = u_x + dx[i]
                    yi = u_y + dy[i]

                    if xi < 0 or xi >= m or yi < 0 or yi >= n:
                        continue

                    if not visited[xi][yi] and grid2[xi][yi] == 1:
                        q.append((xi, yi))
                        visited[xi][yi] = True  # remember this line, otherwise TLE
            return check

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    check = bfs(i, j)
                    # print(f"i: {i}, j: {j}, check: {check}")
                    if check:
                        count += 1

        # print(visited)
        return count
