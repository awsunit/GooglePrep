# Given an integer array nums, 

# find the contiguous subarray within an array 
# (containing at least one number) which has the largest product.

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = 0 if len(nums) == 0 else nums[0]
        cur = 0
        continuous = True
        for i in nums:
            if cur == 0:
                temp = i
                cur = i
            else:
                temp = cur * i
            if temp > mx:
                mx = temp
            elif temp <= cur:
                #  we should bail 
                cur = 0        
        return mx

if __name__ == "__main__":
    s = Solution()
    l = [0,1,-2,-3,-4]
    print(s.maxProduct(l))