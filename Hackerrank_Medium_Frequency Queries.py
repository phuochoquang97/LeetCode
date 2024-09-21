#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the freqQuery function below.
def freqQuery(queries):
    ret = []
    q_map = defaultdict(int)
    val_map = defaultdict(int)
    for q in queries:
        op, val = q
        if op == 1:
            val_map[q_map[val]] = max(val_map[q_map[val]] - 1, 0)
            q_map[val] += 1
            val_map[q_map[val]] += 1
        if op == 2:
            val_map[q_map[val]] = max(val_map[q_map[val]] - 1, 0)
            q_map[val] = max(q_map[val] - 1, 0)
            val_map[q_map[val]] += 1

        if op == 3:
            # check if key with value == val in q_map
            if val_map[val] >= 1:
                ret.append(1)
            else:
                ret.append(0)
    return ret


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write("\n".join(map(str, ans)))
    fptr.write("\n")

    fptr.close()
