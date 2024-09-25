#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def largestRectangle(h):
    # Write your code here
    s = []
    h.append(0)
    max_area = 0

    for i in range(len(h)):
        while s and h[i] < h[s[-1]]:
            height = h[s.pop()]
            width = i if not s else i - s[-1] - 1
            max_area = max(max_area, height * width)
        s.append(i)

    return max_area


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + "\n")

    fptr.close()
