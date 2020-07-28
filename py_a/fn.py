

def findNumber(arr, k):
    try:
        arr.index(k)
        return 'YES'
    except ValueError:
        return 'NO'

def oddNumbers(l, r):

    while l <= r:
        if l % 2:
            # odd
            print(l)
        l += 1
#
# Complete the 'areAlmostEquivalent' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY s
#  2. STRING_ARRAY t
#
from collections import Counter
from itertools import zip_longest
def areAlmostEquivalent(s, t):
    # Write your code here
    # 

    ra = []

    for i in range(len(s)):
        # print(i)
        # get the string
        si = s[i]
        ti = t[i]
        # same length?
        # if len(si) != len(ti):
        #     ra.append('NO')
        #     continue
        # get counts of letters
        si_counts = Counter(si)
        ti_counts = Counter(ti)

        ok = True
        for k,v in si_counts.items():
            if ti_counts.get(k):
                # does contain, compare
                if abs(ti_counts[k] - v) > 3:
                    ok = False
                    break
            else:
                # doesn't contain
                if v > 3:
                    ok = False
                    break



        # zip em up
        # z = list(zip_longest(si_counts.values(), ti_counts.values(), fillvalue=0))
        # ok = True
        # for t1, t2 in z:
        #     if abs(t1 - t2) > 3:
        #         ok = False
        #         break

        v = 'YES' if ok else 'NO'
        ra.append(v)
    


        # print(si_counts)
        # print(ti_counts)
        # print(z, '\n')



    return ra

def getIdealNums(low, high):

    # get our starting indexs?
    x = 0
    y = 0
    # while pow(3,x)*pow(5, y) < low:

    return 0

def partitionArray(k, numbers):

    if len(numbers) % k:
        # not enough letters
        return 'No'

    # how many sub arrays need
    n = int(len(numbers) / k)

    sbr = [[] for i in range(n)]

    for digit in numbers:
        added = False
        for si in sbr:
            if len(si) < k:
                try:
                    si.index(digit)
                except:
                    si.append(digit)
                    added = True
                    break
        if not added:
            return 'No'
            
    return 'Yes'



if __name__ == "__main__":
    # print(findNumber([1,2,3], 5))
    a = ['aabaab', 'aaaaabb']
    b = ['bbabbc', 'abb']
    # a = ['dddd']
    # b = ['klmn']
    # print(areAlmostEquivalent(a, b))
    # print(getIdealNums(200, 405))
    a = [1,2,3,4]
    k = 3
    a = [1,2,2,3]
    print(partitionArray(k, a))