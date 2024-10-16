class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        store = [["a", a], ["b", b], ["c", c]]
        ret = ""
        current_letter = "_"
        while True:
            # find possible letter
            store = sorted(store, key=lambda x: -x[1])
            idx = 0 if store[0][0] != current_letter else 1
            if store[idx][1] == 0:
                return ret

            ret += store[idx][0]

            # update new freq of used letter
            store[idx][1] -= 1

            # update current_letter
            if len(ret) >= 2 and ret[-1] == ret[-2]:
                current_letter = ret[-1]
            else:
                current_letter = "_"

        return ret
