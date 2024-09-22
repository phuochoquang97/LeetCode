#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    # Write your code here
    if k >= (len(s) + len(t)):
        return "Yes"
    i = 0
    while i < min(len(s), len(t)):
        if s[i] == t[i]:
            i += 1
        else:
            break
    min_step = len(s) - i + len(t) - i
    if (k - min_step) % 2 == 0 and (k - min_step) >= 0:
        return "Yes"

    return "No"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + "\n")

    fptr.close()
