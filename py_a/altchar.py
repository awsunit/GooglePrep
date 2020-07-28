import math
import os
import random
import re
import sys
from collections import Counter
# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # get our two chars
    c = Counter(s)
    l = list(c.keys())
    a = l[0]
    t = s
    while re.search(r"{}{}".format(a,a), t):
        t = re.sub(r"{}{}".format(a,a), a, t)
        print(t)
    if len(l) == 2:
        b = l[1]
        while re.search(r"{}{}".format(b,b), t):
            t = re.sub(r"{}{}".format(b,b), b, t)
            print(t)


        

    return  len(s) - len(t)

if __name__ == '__main__':
    fptr = open('lsr.txt', 'w')
    f = open('t_altchar.py', 'r')

    # q = int(input())
    q = int(f.readline().rstrip())

    for q_itr in range(q):
        s = f.readline().rstrip()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()