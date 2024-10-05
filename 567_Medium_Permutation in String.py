class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1

        # init first window
        window_size = len(s1)
        for i in range(window_size):
            window_count[ord(s2[i]) - ord("a")] += 1

        if window_count == s1_count:
            return True

        for i in range(window_size, len(s2)):
            window_count[ord(s2[i]) - ord("a")] += 1
            window_count[ord(s2[i - window_size]) - ord("a")] -= 1

            if window_count == s1_count:
                return True

        return False
