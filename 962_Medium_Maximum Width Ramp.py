class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # find largest j - i with nums[j] >= nums[i]
        # bruteforce -> O(n^2) TLE

        n = len(nums)
        # left min array
        left_min = [0] * n
        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i])

        # right max array
        right_max = [0] * n
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        i, j = 0, 0
        max_diff = -1
        n = len(nums)
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1

        return max_diff