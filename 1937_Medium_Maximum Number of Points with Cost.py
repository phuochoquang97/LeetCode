class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Number of rows (m) and columns (n)
        m, n = len(points), len(points[0])

        # Initialize dp array to store the max points until the previous row
        dp = points[0]

        # Temporary arrays to store left-to-right and right-to-left maximums
        left = [0] * n
        right = [0] * n

        # Iterate over each row starting from the second row
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
