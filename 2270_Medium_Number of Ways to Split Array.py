class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        current_sum = 0
        cummulative_sum = []
        for i in range(n):
            current_sum += nums[i]
            cummulative_sum.append(current_sum)

        count = 0
        for i in range(n - 1):
            if cummulative_sum[i] >= total_sum - cummulative_sum[i]:
                count += 1

        return count
