#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # init the rank -
    ranked = sorted(ranked, reverse=True)
    rank_dict = defaultdict(int)
    rank_idx = 1
    for r in ranked:
        if r not in rank_dict:
            rank_dict[r] = rank_idx
            rank_idx += 1
    list_keys = list(rank_dict.keys())

    # binary search key, find the first key that score >= key
    def binary_search_key(score):
        left = 0
        right = len(list_keys) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if list_keys[mid] >= score:
                left = mid + 1
            else:
                right = mid - 1
            # print(f"left: {left}, right: {right}")
        return left

    ret = []
    for s in player:
        i = binary_search_key(s)
        s_idx = 0
        if i > 0 and list_keys[i - 1] == s:
            s_idx = rank_dict[list_keys[i - 1]]
        elif i >= len(list_keys):
            s_idx = rank_dict[list_keys[-1]] + 1
        else:
            s_idx = rank_dict[list_keys[i]]
        ret.append(s_idx)

    return ret


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
