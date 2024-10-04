class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        n_team = n / 2
        s = sum(skill) / (n_team)
        if s != int(s):
            return -1

        s = int(s)
        m = defaultdict(int)
        chemistry = 0

        for sk in skill:
            if (s - sk) in m and m[s - sk] > 0:
                m[s - sk] -= 1
                chemistry += sk * (s - sk)
            else:
                m[sk] += 1

        for v in m.values():
            if v != 0:
                return -1

        return chemistry
