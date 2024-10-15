class Solution:
    def minimumSteps(self, s: str) -> int:
        right_zero = 0
        ret = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                right_zero += 1
            elif s[i] == "1":
                ret += right_zero

        return ret
