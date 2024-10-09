class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count_open = 0
        count_close = 0
        ret = 0
        for c in s:
            if c == "(":
                count_open += 1
            else:
                count_close += 1
            if count_close > count_open:
                ret += 1
                # insert and update
                count_open += 1

        return ret + count_open - count_close
