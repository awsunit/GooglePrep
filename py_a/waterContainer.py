from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:

		leftPointer = 0
		rightPointer = len(height) - 1
		maxArea = 0

		while leftPointer < rightPointer:
			distance = rightPointer - leftPointer
			leftHeight = height[leftPointer]
			rightHeight = height[rightPointer]
			minHeight = min(leftHeight, rightHeight)

			area = distance * minHeight
			maxArea = max(maxArea, area)

			if rightHeight < leftHeight:
				rightPointer -= 1
			else:
				leftPointer += 1


		return maxArea



height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
s = Solution()
print(s.maxArea(height))