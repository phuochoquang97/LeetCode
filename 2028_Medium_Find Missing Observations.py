class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_m = sum(rolls)
        sum_n = mean * (m + n) - sum_m

        if sum_n < n or sum_n > 6 * n:
            return []

        avg_n = sum_n // n
        # print(f"sum_n: {sum_n}, avg_n: {avg_n}")
        left = sum_n % n
        ret = [avg_n] * n
        i = 0
        while left:
            ret[i] += 1
            left -= 1
            i += 1

        return ret
