class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        robots = [[p, h, l] for p, h, l in zip(positions, healths, directions)]
        robots.sort(key=lambda x: x[0])

        stack = deque()
        for i in range(len(robots)):
            pos, health, direction = robots[i]
            if direction == "L":
                while len(stack) > 0 and stack[-1][2] == "R":  # collision
                    if health > stack[-1][1]:
                        stack.pop()
                        health -= 1
                    elif health == stack[-1][1]:
                        stack.pop()
                        health = 0
                        break
                    else:
                        stack[-1][1] -= 1
                        health = 0
                        break

            if health != 0:
                stack.append([pos, health, direction])

        m = {}
        for s in stack:
            m[s[0]] = s[1]

        ret = []
        for pos in positions:
            if pos in m.keys():
                ret.append(m[pos])

        return ret
