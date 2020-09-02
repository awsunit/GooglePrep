# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞
import math
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        last = -math.inf  
        for i in range(len(nums)):
            if i == len(nums) - 1 and nums[i] > nums[i - 1]:
                return i
            if (last < nums[i] and nums[i] > nums[i + 1]):
                return i
            last = nums[i]

if __name__ == "__main__":
    nums = [1,2,3,1]
    s = Solution()
    print(s.findPeakElement(nums))
          