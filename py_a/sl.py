

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    r = "NO"

    s1_c = Counter(s1)
    s2_c = Counter(s2)

    for s1c in s1_c:
        for s2c in s2_c:
            # only counts > 0
            if s1c == s2c:
                r = "YES"
                break 
    return r

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("lsr.txt", 'w')
    f = open("ls1.txt", 'r')
    # q = int(input())
    q = int(f.readline())

    for q_itr in range(q):
        # s1 = input()
        s1 = f.readline()
        # s2 = input()
        s2 = f.readline()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
