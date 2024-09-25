#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    # Write your code here
    q = deque()
    b_open = ["(", "[", "{"]
    for b in s:
        if b in b_open:
            q.append(b)
        else:
            if len(q) > 0:
                if b == ")" and q[-1] == "(":
                    q.pop()
                elif b == "]" and q[-1] == "[":
                    q.pop()
                elif b == "}" and q[-1] == "{":
                    q.pop()
                else:
                    return "NO"
            else:
                return "NO"
    if len(q) > 0:
        return "NO"

    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + "\n")

    fptr.close()
