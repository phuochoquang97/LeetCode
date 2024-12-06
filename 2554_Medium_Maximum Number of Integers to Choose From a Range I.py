"""
You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.
"""


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        set_banned = set(banned)  # to make O(1) for checking
        current_sum = 0
        count = 0
        for i in range(1, n + 1):
            if i not in set_banned:
                if current_sum + i <= maxSum:
                    current_sum += i
                    count += 1
                else:
                    return count

        return count
