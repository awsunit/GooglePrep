from collections import Counter
from typing import List
from functools import reduce

def merge(l1, l2):
    # match on key
    matchingkeys = l1.keys() & l2.keys()
    # print(matchingkeys)
    r = {}
    for k in matchingkeys:
        m = min(l1[k], l2[k])
        r[k] = m

    return r

    
class Solution:
    

    def commonChars(self, A: List[str]) -> List[str]:
                
        # map of string to map of char and counts
        mp = {}
        lst = []
        for s in A:
            counts = dict(Counter(s))
            lst.append(counts)

        r = reduce(merge, lst)
        print(r)

        r1 = []
        for k,v in r.items():
            for i in range(v):
                r1.append(k)
        return r1

        # would like to reduce this to a map char -> list where:
        # list contains all possible occurance rates of char

        # The Following ~Works

        # first = set(lst[0].items())
        # # print(first)
        # lst = lst[1:]
        # # print(lst)

        # for l in lst:
        #     first = first & set(l.items())

        # r = []
        # for k,v in first:
        #     for i in range(v):
        #         r.append(k)

        # return r
        
if __name__ == "__main__":
    l = ["bella", "label", "roller"]
    l = ["cool", "lock", "cook"]
    s = Solution()
    print(s.commonChars(l))