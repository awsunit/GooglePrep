

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    arr = [0] + arr
    cur = len(arr) - 1

    # for all cur, c, seen:
    #   arr[c] == c
    while cur > 0:
        if arr[cur] == cur:
            cur -= 1
            continue

        nxt = cur - 1
        # how far are the nodes from their respective homes
        cdst = abs(cur - arr[cur])
        ndst = abs(nxt - arr[nxt])
        tdst = cdst + ndst
        while nxt > 0:
            if (abs(cur - arr[nxt]) + abs(nxt - arr[cur])) < tdst:
                t = arr[nxt]
                arr[nxt] = arr[cur]
                arr[cur] = t
                swaps += 1
                break
            nxt -= 1
        cur -= 1
        




    return swaps



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    f = open('ls1.txt', 'r')
    fptr = open('lsr.txt', 'w')

    # n = int(input())
    n = int(f.readline())
    print(n)

    # arr = list(map(int, input().rstrip().split()))
    arr = list(map(int, f.readline().rstrip().split()))

    r = minimumSwaps(arr)

    fptr.write(str(r) + '\n')

    fptr.close()
