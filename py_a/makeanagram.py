import math
import os
import random
import re
import sys
from collections import Counter
from itertools import zip_longest
from string import ascii_lowercase


def p(a):
    print(a)

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    # get counts

    a_counts = Counter(ascii_lowercase)
    b_counts = Counter(ascii_lowercase)

    # p(a_counts)
    # p(b_counts)

    a_counts.update(a)
    b_counts.update(b)

    # p(a_counts)
    # p(b_counts)
    z = list(zip(a_counts.values(), b_counts.values()))
    # p(z)
    f = list(filter(lambda x : x[0] != x[1], z))
    p(f)
    count = 0
    for t1,t2 in f:
        count += abs(t1 - t2)

    p(count)

    return count

    # we are trying to map counts of equal characters
    

    # abc = zip_longest(ac, bc)

    # f = list(filter(lambda x, y : ))

if __name__ == '__main__':
    fptr = open('lsr.txt', 'w')

    # a = input()

    # b = input()
    a = "ccc"
    b = "ccce"

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
