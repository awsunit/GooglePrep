from typing import List

# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k


# solution notes
# can't sort the array, since that changes which indices we are talking about...




#  the following is a brute force solution
# class Solution:
# 	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
# 		start = 0
# 		end = 1

# 		if len(nums) <= 0:
# 			return False

# 		while (start < len(nums)):
# 			# move our right pointer right, until our k condition is
# 			# watch for right pointer to go out of bounds
# 			while abs(start - end) <= k:
# 				if end == len(nums):
# 					# we need to break or something
# 					break
# 				if nums[start] == nums[end]:
# 					return True
# 				# else they didn't equal true
# 				end += 1

# 			start += 1
# 			end = start + 1
# 		return False

class Solution:



	#  too slow with a list
	# def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
	# 	start = 0

	# 	if len(nums) < 2 or k < 1:
	# 		return False

	# 	# get the first range figured out
	# 	x = k if start + k < len(nums) else len(nums) - 1
	# 	ranges_numbers = self.getNums(nums, start, k)

	# 	while start < len(nums):
	# 		current_number = nums[start]

	# 		for num in ranges_numbers:
	# 			if num == current_number:
	# 				return True
	# 		# remove first value from array, plug us in
	# 		ranges_numbers.pop(0)
	# 		ranges_numbers.append(current_number)
	# 		start += 1

	# 	return False

	def getNums(self, nums: List[int], numberToGrab: int) -> dict:
		final_list = {}
		while numberToGrab >= 0:
			current_number = nums[numberToGrab]
			if current_number in final_list:
				final_list[current_number] += 1
			else:
				final_list[current_number] = 1
			numberToGrab -= 1

		# print(final_list)
		return final_list


	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		start = 0

		if len(nums) < 2 or k < 1:
			return False

		# get the first range figured out
		x = k if k < len(nums) else len(nums) - 1
		ranges_numbers = self.getNums(nums, x)

		for numby,v in ranges_numbers.items():
			if v > 1:
				return True

		start = k + 1

		while start < len(nums):
			current_number = nums[start]
			index_to_delete = start - k - 1
			# print('start: {}, curren_nu: {}, index_to_delete: {}, val_at_index: {}'.format(start, current_number, index_to_delete, nums[index_to_delete]))
			ranges_numbers[nums[index_to_delete]] -= 1

			if current_number in ranges_numbers:
				if ranges_numbers[current_number] > 0:
					return True
				ranges_numbers[current_number] += 1
			else:
				ranges_numbers[current_number] = 1
			start += 1

		return False







solution = Solution()
myList = [4,1,2,3,1,5]
k = 3
myList = [1,2,3,1,2,3]
k = 2
myList = [1,0,1,1]
k = 1
myList = [1,2,3,1]
k = 3

print(solution.containsNearbyDuplicate(myList, k))