class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # split hour and minutes
        time_value = []
        for tp in timePoints:
            h, m = tp.split(":")
            time_value.append((int(h), int(m)))

        time_value = sorted(time_value)

        ret = sys.maxsize
        n = len(timePoints)
        for i in range(n - 1):
            # calculate diff between time_value[i] and time_value[i+1]
            h_diff = time_value[i + 1][0] - time_value[i][0]
            if time_value[i + 1][1] >= time_value[i][1]:
                m_diff = time_value[i + 1][1] - time_value[i][1]
            else:
                m_diff = 60 + time_value[i + 1][1] - time_value[i][1]
                h_diff -= 1
            ret = min(ret, h_diff * 60 + m_diff)

        # calculate diff between time_value[0] and time_value[-1]
        h_diff = 24 - time_value[-1][0] - 1 + time_value[0][0]
        m_diff = 60 - time_value[-1][1] + time_value[0][1]
        ret = min(ret, h_diff * 60 + m_diff)

        return ret
