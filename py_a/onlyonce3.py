from typing import List
from collections import Counter



class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        l = list(x for x,y in c.items() if y == 1)

        # [print(x,y) for x,y in c.items()]
        return l

if __name__ == "__main__":
    a = [1,1,2,2,3,4,4,5]
    b = [1,2,3,4,4,3,2,5]

    s = Solution()

    l = s.singleNumber(a)

    print(l)

    l = s.singleNumber(b)
    print(l)
    