import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0

    a = 0
    sz = len(arr)

    num_locs = {}

    for i in range(len(arr)):
        e = arr[i]
        if not num_locs.get(e):
            num_locs[e] = [i]
        else:
            num_locs[e].append(i)


    print(num_locs)


    for ikv in num_locs:

        print(ikv)

        # v +=




    return count



    # while a < sz - 2:
    #     b = a + 1
    #     while b < sz - 1:
    #         c = b + 1
    #         while c < sz:
    #             ra = arr[a]
    #             rb = arr[b]
    #             rc = arr[c]
    #             # print(ra,rb,rc)

    #             i = 1 if  r == 1 else int(math.log(ra, r))
    #             j = 2 if r == 1 else int(math.log(rb, r))
    #             k = 3 if r == 1 else int(math.log(rc, r))

    #             # print(i,j,k)
    #             if j == i + 1:
    #                 if k == j + 1:
    #                     count += 1

    #             c += 1

    #         b += 1
        
    #     a += 1

    # # [print(k,v) for k,v in m.items()]

    # return count

if __name__ == '__main__':
    fptr = open('lsr.txt', 'w')
    f = open('ls1.txt', 'r')
    
    nr = f.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, f.readline().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()


    # count = 0

    # a = 0
    # sz = len(arr)

    # m = {}

    # while a < sz - 2:
    #     b = a + 1
    #     while b < sz - 1:
    #         c = b + 1
    #         while c < sz:
    #             ra = arr[a]
    #             rb = arr[b]
    #             rc = arr[c]
    #             # print(ra,rb,rc)

    #             i = 1 if  r == 1 else int(math.log(ra, r))
    #             j = 2 if r == 1 else int(math.log(rb, r))
    #             k = 3 if r == 1 else int(math.log(rc, r))

    #             # print(i,j,k)
    #             if j == i + 1:
    #                 if k == j + 1:
    #                     count += 1

    #             c += 1

    #         b += 1
        
    #     a += 1

    # # [print(k,v) for k,v in m.items()]

    # return count