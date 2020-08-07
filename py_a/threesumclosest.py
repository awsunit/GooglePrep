from typing import List
from itertools import combinations
class Solution:

    # def inner(self, nums, index, target, closest):


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = 4000000
        c = combinations(nums, 3)

        for combo in c:
            # print(combo)
            # print(sum(combo))
            t1 = abs(target - sum(combo))
            t2 = abs(target - closest)
            # print(t1, t2)
            if abs(t1) < abs(t2):
                closest = sum(combo)

        return closest

def sub(i):
    i = l[0]
    l[0] = i - 1
if __name__ == "__main__":
    l = [1,1,-1,-1,3]
    print(Solution().threeSumClosest(l, 3))

    # i = 8
    # l = [i]
    # sub(l)
    # print(sub(i))
    m = map(lambda x: x + 100, l)
    print(list(m))