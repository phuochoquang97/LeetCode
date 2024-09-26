#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    neighbors_dict = defaultdict(list)

    n_row = len(grid)
    n_col = len(grid[0])
    # neighbors for each row
    for row in range(n_row):
        for i in range(0, n_col - 1):
            if grid[row][i] == "X":
                continue
            for j in range(i + 1, n_col):
                if grid[row][j] == ".":
                    neighbors_dict[(row, i)].append((row, j))
                    neighbors_dict[(row, j)].append((row, i))
                else:
                    break

    for col in range(n_col):
        for j in range(0, n_row - 1):
            if grid[j][col] == "X":
                continue
            for i in range(j + 1, n_row):
                if grid[i][col] == ".":
                    neighbors_dict[(j, col)].append((i, col))
                    neighbors_dict[(i, col)].append((j, col))
                else:
                    break
    # print(neighbors_dict)
    distance_map = defaultdict(int)
    # init distance map
    for i in range(n_row):
        for j in range(n_col):
            distance_map[(i, j)] = sys.maxsize

    distance_map[(startX, startY)] = 0
    q = deque()
    q.append((startX, startY))

    while q:
        u_x, u_y = q.popleft()
        for neighbor in list(neighbors_dict[(u_x, u_y)]):
            nx, ny = neighbor
            distance_map[(nx, ny)] = min(
                distance_map[(nx, ny)], distance_map[(u_x, u_y)] + 1
            )
            neighbors_dict[(nx, ny)].remove((u_x, u_y))
            neighbors_dict[(u_x, u_y)].remove((nx, ny))
            q.append((nx, ny))
    # print(distance_map)
    return distance_map[goalX, goalY]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + "\n")

    fptr.close()
