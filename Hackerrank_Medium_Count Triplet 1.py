#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import bisect


def count_less_than(arr, x):
    return bisect.bisect_left(arr, x)


def count_greater_than(arr, x):
    return len(arr) - bisect.bisect_right(arr, x)


# Complete the countTriplets function below.
def countTriplets(arr, r):
    # map the index of each value in arr O(n)
    arr_map = defaultdict(list)
    for i in range(len(arr)):
        arr_map[arr[i]].append(i)
    arr_set = set(arr)
    total_triplets = 0
    for v in arr_set:
        i_indices = arr_map[v]
        j_indices = arr_map[v * r]
        if not j_indices:
            continue
        k_indices = arr_map[v * r * r]
        if not k_indices:
            continue

        # TODO: process i, j, k here
        i_indices.sort()
        j_indices.sort()
        k_indices.sort()

        for j in j_indices:
            i_count = count_less_than(i_indices, j)
            k_count = count_greater_than(k_indices, j)
            total_triplets += i_count * k_count
    return total_triplets


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + "\n")

    fptr.close()
