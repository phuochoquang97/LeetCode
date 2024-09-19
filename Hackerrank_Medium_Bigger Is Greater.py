#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def biggerIsGreater(w):
    # Write your code here
    w_list = list(w)
    w_list_sorted = sorted(w_list, reverse=True)
    if w_list == w_list_sorted:
        return "no answer"

    # find the longest increasing string, starting from last index
    idx = len(w) - 1
    while idx > 0 and w[idx - 1] >= w[idx]:
        idx -= 1

    ret = list(w[:idx])

    # TODO
    # swap w[idx-1] with the smallest char in w[idx:]
    # that is greater than w[idx-1]
    temp = ret[idx - 1]
    w_from_idx = sorted(list(w[idx:]))
    i = 0
    while temp >= w_from_idx[i] and i < len(
        w_from_idx
    ):  # find character in w[idx:] to swap
        i += 1
    ret[idx - 1] = w_from_idx[i]  # swap
    w_from_idx[i] = temp

    w_from_idx = sorted(w_from_idx)
    ret.extend(w_from_idx)

    return "".join([r for r in ret])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + "\n")

    fptr.close()
