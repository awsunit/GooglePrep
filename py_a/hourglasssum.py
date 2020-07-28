

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    r = []

    for row in range(6):
        for col in range(6):
            if row != 0 and row !=  5 and col != 0 and col != 5:
                a = arr[row][col]
                b = arr[row-1][col-1]
                c = arr[row-1][col]
                d = arr[row-1][col+1]
                e = arr[row+1][col-1]
                f = arr[row+1][col]
                g = arr[row+1][col+1]
                
                r.append((a + b + c + d + e + f + g))

    return r

if __name__ == '__main__':
    fptr = open('lsr.txt', 'w')


    arr = []

    f = open("ls.txt", 'r')

    for _ in range(6):
        arr.append(list(map(int, f.readline().rstrip().split())))

        # arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    result = max(result)

    fptr.write(str(result) + '\n')

    fptr.close()
