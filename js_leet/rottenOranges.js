// You are given an m x n grid where each cell can have one of three values:

//     0 representing an empty cell,
//     1 representing a fresh orange, or
//     2 representing a rotten orange.

// Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

// Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
	let minutes = 0;

	let indexesToTurnRotten = [];
	while (true) {
		// go through grid and covert fresh to rotten
		grid.forEach((row, row_i) => {
			// console.log(row);
			row.forEach((column, c_i) => {
				if (column == 2) {
					// it's rotting and we should convert it's neighbors BUT SKIP THEM WHEN LOOKING
					// top, bottom, left, right
					let ur = row_i == 0 ? -1 : row_i - 1;
					let dr = row_i == grid.length - 1 ? -1 : row_i + 1;
					let lc = c_i == 0 ? -1 : c_i - 1;
					let rc = c_i == grid[0].length - 1 ? -1 : c_i + 1;
					indexesToTurnRotten.push([ur, c_i],[dr, c_i],[row_i, lc],[row_i, rc]);
				}
			});
		});

		let applesTurnedRotten = false;
		indexesToTurnRotten.forEach((indexArray) => {
			if (indexArray[0] != -1 && indexArray[1] != -1) {
				if (grid[indexArray[0]][indexArray[1]] == 1) {
					grid[indexArray[0]][indexArray[1]] = 2;
					applesTurnedRotten = true;
				}
			}
		});

		// check for any remaining fresh apples
		let freshApplesRemain = false;
		for (var r = 0; r < grid.length; r++) {
			for (var c = 0; c < grid[0].length; c++) {
				if (grid[r][c] == 1) {
					freshApplesRemain = true;
					break;
				}
			}
		}

		if (!applesTurnedRotten) {
			if (!freshApplesRemain) {
				return minutes;
			}
			return -1;
		}

		indexesToTurnRotten.length = 0;
		minutes++;
	}
};

let grid = [
	[2, 1, 1],
	[1, 1, 0],
	[0, 1, 1],
];
// grid = [[2,1,1],[0,1,1],[1,0,1]];

// grid = [[0,2]];

console.log(orangesRotting(grid));
