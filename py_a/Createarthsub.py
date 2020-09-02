# Given an array of numbers arr. A sequence of numbers is called an arithmetic progression 
# if the difference between any two consecutive elements is the same.

# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # sort, then go through
        arr.sort()
        spot = 2
        diff = arr[1] - arr[0]
        l = len(arr)
        while (spot < l):
            if arr[spot] - arr[spot-1] != diff:
                return False
            spot += 1
        return True
        
        
if __name__ == "__main__":
    a = [1,2,4]
    # a = [1,3,2]
    s = Solution()
    print(s.canMakeArithmeticProgression(a))