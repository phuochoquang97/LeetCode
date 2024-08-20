class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # row i-1: dp_0, dp_1,..., dp_n
        # row i  : ... , dp_j,..., ...
        # dp[i][j] = max(dp[i-1][k] - abs(k-j)) for k in range(0, n)
        # with this case, we need to loop m rows, n cols, for each dp[i][j], we need to calculate n times
        # => time complexity is O(m*n*n) => TLE
        # => need to optimize

        # row i-1: dp_0, dp_1, dp_2, dp_3,...
        # row i  :
        # From left to right:
        #     - dp[i][3] = max(dp_3, dp_2 - 1, dp_1 - 2, dp_0 - 3)
        #     - dp[i][2] = max(dp_2, dp_1 - 1, dp_0 - 2)
        #     => we see the pattern: dp[i][3] = max(dp[i][2] - 1, dp_3)
        #     => generalize: dp[i][j] = max(dp[i][j-1] - 1, dp[i-1][j])

        m, n = len(points), len(points[0])

        dp = points[0]  # dp is to store the max of sum until row i - 1

        # left and right are to calculate the dp of the current row
        left = [0] * n
        right = [0] * n

        for i in range(1, m):
            # Calculate the left max array
            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, dp[j])

            # Calculate the right max array
            right[n - 1] = dp[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, dp[j])

            # Update dp for the current row using the maximum of left and right arrays
            for j in range(n):
                dp[j] = points[i][j] + max(left[j], right[j])

        # The result is the maximum value in the dp array after processing all rows
        return max(dp)
