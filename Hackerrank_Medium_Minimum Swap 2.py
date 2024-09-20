#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count_step = 0
    # create a map
    idx_map = defaultdict()
    for i in range(len(arr)):
        idx_map[arr[i]] = i
    # print(f"idx_map: {idx_map}")

    for i in range(len(arr)):
        if arr[i] == i + 1:
            continue
        # swap value at index i with index of value i
        temp = arr[i]
        idx_value_i = idx_map[i + 1]
        # print(f"i: {i}, arr[i]: {arr[i]}, idx_value_i: {idx_value_i}")
        arr[i] = arr[idx_value_i]
        arr[idx_value_i] = temp
        # update map
        idx_map[arr[i]] = i
        idx_map[arr[idx_value_i]] = idx_value_i
        count_step += 1

    return count_step


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + "\n")

    fptr.close()
