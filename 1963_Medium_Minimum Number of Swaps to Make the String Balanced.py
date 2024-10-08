class Solution:
    def minSwaps(self, s: str) -> int:
        open_idx = []
        for i, c in enumerate(s):
            if c == "[":
                open_idx.append(i)
        count_open = 0
        count_close = 0
        ret = 0
        sl = list(s)
        for i in range(len(sl)):
            if sl[i] == "]":
                count_close += 1
            else:
                count_open += 1
            if count_close > count_open:
                # swap
                temp = sl[i]
                sl[i] = sl[open_idx[-1]]
                sl[open_idx[-1]] = temp
                open_idx.pop()
                ret += 1
                # update count
                count_close -= 1
                count_open += 1

        return ret
