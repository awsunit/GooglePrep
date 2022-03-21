// Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

//     All the visited cells of the path are 0.
//     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

// The length of a clear path is the number of visited cells of this path.

// Input: grid = [[0,1],[1,0]]
// Output: 2

let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];

//ul,ur,bl,br
let ddr = [-1, -1, 1, 1];
let ddc = [-1, 1, -1, 1];

const CLEAR_PATH = 0;
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function (grid) {
	if (grid[0][0] != CLEAR_PATH) return -1;

	// shortest path requirement indicates a BFS with level order traversal
	let queue = [];
	let visited = new Map();
	visited.set(`0,0`, true);

	queue.push([0, 0]);

	let pathCount = 0;

	while (queue.length > 0) {
		pathCount += 1;
		// level order
		let amountToPullFromQueue = queue.length;

		while (amountToPullFromQueue-- > 0) {
			let [row, column] = queue.shift();

			if (row == grid.length - 1 && column == grid[0].length - 1) {
				return pathCount;
			}

			// okay it wasn't the node we wanted, is it one that we could traverse though?
			if (grid[row][column] == CLEAR_PATH) {
				for (var i = 0; i < dr.length; i++) {
					let nr = row + dr[i];
					let nc = column + dc[i];
					let nkey = `${nr},${nc}`;
					// within bounds, havent seen before, clear path
					if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || visited.has(nkey) || grid[nr][nc] != CLEAR_PATH) continue;
					visited.set(nkey, true);
					queue.push([nr,nc]);
				}
				for (var i = 0; i < ddr.length; i++) {
					let nr = row + ddr[i];
					let nc = column + ddc[i];
					let nkey = `${nr},${nc}`;
					// within bounds, havent seen before, clear path
					if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || visited.has(nkey) || grid[nr][nc] != CLEAR_PATH) continue;
					visited.set(nkey, true);
					queue.push([nr,nc]);
				}
			} else {
				// we can't go anywhere from here
			}
		}
	}

	return -1;
};

let grid = [
	[0, 1],
	[1, 0],
];

// grid = [[0,0,0],[1,1,0],[1,1,0]];

// grid = [[1,0,0],[1,1,0],[1,1,0]];

console.log(shortestPathBinaryMatrix(grid));
