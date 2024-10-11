class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                if nums[i] < nums[stack[-1]]:
                    stack.append(i)

        max_diff = -1
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_diff = max(max_diff, j - stack[-1])
                stack.pop()

        return max_diff
