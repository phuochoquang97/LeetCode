from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        nb_pairs = 0
        nb_subarrays = 0
        n = len(nums)
        right = 0

        for left in range(n):
            # Expand right to satisfy the condition
            while right < n and nb_pairs < k:
                nb_pairs += freq[nums[right]]
                freq[nums[right]] += 1
                right += 1

            # If we have enough pairs, every subarray from [left..right-1] to [left..n-1] is valid
            if nb_pairs >= k:
                nb_subarrays += n - right + 1

            # Shrink window from left
            freq[nums[left]] -= 1
            nb_pairs -= freq[nums[left]]

        return nb_subarrays
