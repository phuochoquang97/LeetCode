class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        # do not do this dp = [[0] * n] * m
        dx = [-1, 0, 1]
        max_move = 0

        for c in range(1, n):
            for r in range(m):
                for k in range(3):
                    r_k = r + dx[k]
                    c_k = c - 1
                    if r_k < 0 or r_k >= m or c_k < 0 or c_k >= n:
                        continue
                    if (grid[r][c] > grid[r_k][c_k]) and (dp[r_k][c_k] == c_k):
                        dp[r][c] = dp[r_k][c_k] + 1
                        max_move = max(max_move, dp[r][c])

        return max_move
