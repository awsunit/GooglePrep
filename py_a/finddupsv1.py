from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = {}
        
        for n in nums:
            if c.get(n):
                c[n] += 1
            else:
                c[n] = 1

        r = [x for x,y in c.items() if y > 1]
        return r


if __name__ == "__main__":
    l = [4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(l))