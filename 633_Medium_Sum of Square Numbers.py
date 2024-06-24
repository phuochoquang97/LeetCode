class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False

        left = 0
        right = int(sqrt(c))

        while left <= right:
            current_sum = left**2 + right**2
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1

        return False
