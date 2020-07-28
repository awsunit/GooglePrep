

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [0] + q
    bribes = 0
    size = len(q)
    counts = {i:2 for i in range(1, size + 1)}
    # i start from furthest size - 2
    i = size - 2
    while i > 0:
        while q[i] > i:
            if counts[q[i]] == 0:
                return -1
            # swap
            counts[q[i]] -= 1
            t = q[i]
            q[i] = q[i+1]
            q[i+1] = t
            bribes += 1
            i += 1
        i -= 1
    return bribes

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))


        v = minimumBribes(q)
        if v == -1:
            print("Too chaotic")
        else:
            print(v)
