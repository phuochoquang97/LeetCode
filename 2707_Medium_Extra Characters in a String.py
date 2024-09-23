class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        s_mod = "_" + s
        dp = [sys.maxsize] * len(s_mod)
        dp[0] = 0
        for i in range(1, len(dp)):
            for word in dictionary:
                cond1 = (i - len(word)) >= 0
                cond2 = word in s_mod[i - len(word) + 1 : i + 1]
                if cond1 and cond2:
                    dp[i] = min(dp[i - len(word)], dp[i])
                dp = min(dp[i], dp[i - 1] + 1)
        return dp[-1]
