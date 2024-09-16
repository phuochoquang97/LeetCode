class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        indies = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        current_mask = 0
        store = {0: -1}

        ret = 0
        for i in range(len(s)):
            if s[i] in indies:  # update current_mask
                current_mask = current_mask ^ indies[s[i]]
            if current_mask in store:
                ret = max(ret, i - store[current_mask])
            else:
                store[current_mask] = i

        return ret
