class Solution:
    def orangeRotting(self, grid: List[List[int]]) -> int:
        q = deque()  # keep track of current rotting oranges
        time = 0
        fresh = 0  # keep track of current fresh oranges

        n_row = len(grid)
        n_col = len(grid[0])

        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:
            l = len(q)
            for i in range(l):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col

                    # check bounding and fresh orange
                    if r < 0 or r == n_row or c < 0 or c == n_col or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2  # assign as a rotten orange
                    q.append([r, c])  # add rotten orange to queue
                    fresh -= 1  # decrease number of fresh oranges
            time += 1

        return time if fresh == 0 else -1
