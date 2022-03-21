# Given an m x n binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.
from typing import List






def maximalSquare( matrix: List[List[str]]) -> int:
	print('')

	max_square = 0
	left_and_up_neighbors = []
	# get our initial counts
	for row in range(len(matrix)):
		new_row = []
		for col in range(len(matrix[0])):
			new_row.append([0,0])
		left_and_up_neighbors.append(new_row)

	# build up a map that has a square's area saved in the bottom right corner
	for row_index, row in enumerate(matrix):
		for column_index, value in enumerate(row):
			neighbor_values_plus_one = [0,0]


			if row_index != 0 and column_index != 0:
				# we need to check both neighbors
				if value == '1':
					# check left
					neighbor_values_plus_one[0] = 1 + left_and_up_neighbors[row_index][column_index - 1][0]
					# check top
					neighbor_values_plus_one[1] = 1 + left_and_up_neighbors[row_index - 1][column_index][1]
			elif row_index == 0 and column_index == 0:
				if value == '1':
					neighbor_values_plus_one = [1,1]
			elif row_index == 0:
				# we don't check north
				if value == '1':
					neighbor_values_plus_one[0] = 1 + left_and_up_neighbors[row_index][column_index-1][0]
					neighbor_values_plus_one[1] = 1
			else:
				#  column_index == 0
				# we don't check west
				if value == '1':
					neighbor_values_plus_one[0] = 1
					neighbor_values_plus_one[1] = 1 + left_and_up_neighbors[row_index - 1][column_index][1]


			# update our counts for the next spot to evaluate
			left_and_up_neighbors[row_index][column_index] = neighbor_values_plus_one

	# find the max of the map's [row_i][col_i][0]  * [row_i][col_i][1]

	for row_index in range(len(matrix)):
		for column_index in range(len(matrix[0])):
			max_square = max(max_square, left_and_up_neighbors[row_index][column_index][0] * left_and_up_neighbors[row_index][column_index][1])

	return max_square



# read file line by line
# create array of 0|1 for each line

matrix = []

data = open('./testcases/product_defect.txt', 'r')

for line in data:
	new_row = [str(int(s)) for s in line.split(',')]
	print(new_row)
	matrix.append(new_row)

print(maximalSquare(matrix))









