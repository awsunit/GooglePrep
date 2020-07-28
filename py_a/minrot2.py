from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = sorted(nums)

        return min(l)


if __name__ == "__main__":
    a = [2,2,2,0,1]
    s = Solution()
    c = s.findMin(a)

    print(c)