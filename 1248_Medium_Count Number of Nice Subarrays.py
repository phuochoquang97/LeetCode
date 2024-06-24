class Solution:
    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        nums = [num % 2 for num in nums]
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = (
            1  # Initialize to handle the case where a subarray starts from index 0
        )
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_counts:
                count += prefix_counts[prefix_sum - goal]
            prefix_counts[prefix_sum] += 1

        return count
