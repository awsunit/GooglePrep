

import math
import os
import random
import re
import sys
from string import ascii_lowercase

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    w_begin = 0
    sz = len(s)
    count = 0

    while w_begin < sz - 1:
        b_begin = w_begin + 1

        while b_begin < sz:
            w_c = {c:0 for c in ascii_lowercase}
            b_c = {c:0 for c in ascii_lowercase}

            w_end = w_begin
            b_end = b_begin

            while  b_end < sz:
                # log counts
                w_c[s[w_end]] += 1
                b_c[s[b_end]] += 1

                ama = True
                for k,v in w_c.items():
                    if v != b_c[k]:
                        ama = False
                        break
                if ama:
                    # print the sub
                    print(w_begin, w_end, b_begin, b_end)
                    count += 1
                
                w_end += 1
                b_end += 1

            b_begin += 1

        w_begin += 1


        
    return count



if __name__ == '__main__':
    # bugs discovered: 
    # when reading from a file: remove \n characters at end of line

    fptr = open('lsr.txt', 'w')

    f = open("ls1.txt", "r")

    q = int(f.readline())
    print("q: {}".format(q))

    while q > 0:
        s = f.readline().rstrip()
        print(s)
        result = sherlockAndAnagrams(s)
        print(result)
        fptr.write(str(result) + '\n')

        q -= 1

    fptr.close()
    f.close()


    # fptr = open('os.environ['OUTPUT_PATH']', 'w')


    # q = int(input())

    # for q_itr in range(q):
    #     s = input()

    #     result = sherlockAndAnagrams(s)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
