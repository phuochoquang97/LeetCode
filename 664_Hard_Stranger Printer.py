class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        - input: string s:
        - index: 0 1 2 3 4 5 6 7
        - s    : a _ _ _ _ a _ _
        - define dp[i][j] is the cost to print from i to j
        -> dp[0][7] = dp[0][4] + dp[5][7] ~ dp[i][j] = dp[i][k-1] + dp[k+1][i], we don't need to count "a" at k index
        - but what if s: a _ _ _ _ _ _?
        -> dp[i][j] = dp[i+1][j] + 1
        """

        n = len(s)

        dp = [[sys.maxsize] * n for _ in range(n)]

        # the cost to print string from index i to i ~ print one character = 1
        for i in range(n):
            dp[i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1  # a trick to cover all pairs of i and j
                # ex: n = 6, l = 2, i in range(0, 6 - 2 + 1 = 5), j from 0 + 2 - 1 = 1 to 4 + 2 - 1 = 5
                # -> 0-1, 1-2, 2-3, 3-4, 4-5
                # -> l = 3, i in range(0, 4), j from 2 to 5 -> 0-2, 1-3, 2-4, 3-5

                # print i-th character separately
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        dp[i][j] = min(
                            dp[i][j], dp[i][k - 1] + (dp[k + 1][j] if j > k else 0)
                        )

        return dp[0][n - 1]
