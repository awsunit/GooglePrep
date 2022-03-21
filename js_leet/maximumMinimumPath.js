// Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

// The score of a path is the minimum value in that path.

//     For example, the score of the path 8 → 4 → 5 → 9 is 4.

// 	Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
// Output: 4
// Explanation: The path with the maximum score is highlighted in yellow.

/**
 * @param {number[][]} grid
 * @return {number}
 */
 var maximumMinimumPath = function(grid) {
	 let dynamicGrid = [];

	 grid.forEach((row, r_i) => {
		let nextRow = [];
		let prevRow = r_i == 0 ? undefined : dynamicGrid[r_i - 1];
		row.forEach((column, c_i) => {
			if (c_i == 0 && r_i == 0) {
				// first value, append us
				nextRow.push(column);
			} else if (c_i == 0) {
				// only check person above us
				let aboveValue = prevRow[c_i];
				nextRow.push(Math.min(column, aboveValue));
			} else if (r_i == 0) {
				// only check the person to our left
				let leftValue = nextRow[c_i - 1];
				nextRow.push(Math.min(leftValue, column));
			} else {
				// check above us and below us
				let aboveValue = prevRow[c_i];
				let leftValue = nextRow[c_i - 1];
				// we want to use the max value from these
				let valueToUse = Math.max(aboveValue, leftValue);
				nextRow.push(Math.min(aboveValue, valueToUse));
			}
		});
		dynamicGrid.push(nextRow);
	 });

	 // last row, penultimate column AND punultimate row last column
	 return Math.max(dynamicGrid[dynamicGrid.length - 1][dynamicGrid[0].length - 2], dynamicGrid[dynamicGrid.length - 2][dynamicGrid[0].length - 1]);
};

let grid = [[5,4,5],[1,2,6],[7,4,6]];
grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]];
grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]];
console.log(maximumMinimumPath(grid));