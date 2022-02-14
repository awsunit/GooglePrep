# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = (nums[0], nums[0])
        final_max = nums[0]

        for num in range(1,len(nums)):
            best = max(current[0], current[1])
            current = (best + nums[num], nums[num])
            # print(current)
            final_max = max(final_max, current[0], current[1])
            # print(final_max)
        return final_max