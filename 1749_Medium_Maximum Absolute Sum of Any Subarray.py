class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = nums[0]
        max_abs_sum = abs(nums[0])

        for i in range(1, len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            min_sum = min(min_sum + nums[i], nums[i])

            max_abs_sum = max(max_abs_sum, abs(max_sum), abs(min_sum))

        return max_abs_sum
