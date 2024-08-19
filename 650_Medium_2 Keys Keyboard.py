class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:  # basecase
            return 0

        i = 2  # find the minimum number of pasting
        while n % i != 0:
            i += 1

        n /= i  # the root for pasting

        return i + self.minSteps(n)
