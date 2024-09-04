class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for ob in obstacles:
            obs.add((ob[0], ob[1]))

        current_dir = "N"
        current_pos = [0, 0]
        max_dis = 0

        right_dict = {"N": "E", "E": "S", "W": "N", "S": "W"}
        left_dict = {"N": "W", "E": "N", "S": "E", "W": "S"}
        direction_map = {"N": (0, 1), "E": (1, 0), "W": (-1, 0), "S": (0, -1)}

        for cmd in commands:
            if cmd == -1:  # turn right
                current_dir = right_dict[current_dir]
            elif cmd == -2:  # return left
                current_dir = left_dict[current_dir]
            else:
                for _ in range(cmd):
                    delta_x, delta_y = direction_map[current_dir]
                    current_pos[0] += delta_x
                    current_pos[1] += delta_y

                    if tuple(current_pos) in obs:
                        current_pos[0] -= delta_x
                        current_pos[1] -= delta_y
                        break

            # print(f"cmd: {cmd}, current_dir: {current_dir}, current_pos: {current_pos}")
            max_dis = max(max_dis, current_pos[0] ** 2 + current_pos[1] ** 2)

        return max_dis
