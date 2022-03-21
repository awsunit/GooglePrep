// You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

//     0 means the cell cannot be walked through.
//     1 represents an empty cell that can be walked through.
//     A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.

// In one step, you can walk in any of the four directions: north, east, south, and west.
// If you are standing in a cell with a tree, you can choose whether to cut it off.

// You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

// Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

// You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

// Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
// Output: 6
// Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];
/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function (forest) {
	// first we need to find the order in which we must operate
	let treesToCut = [];
	forest.forEach((rowOfTrees, r_i) => {
		rowOfTrees.forEach((treeHeight, c_i) => {
			if (forest[r_i][c_i] > 1) {
				treesToCut.push([treeHeight, [r_i, c_i]]);
			}
		});
	});
	// sort ascending
	treesToCut = treesToCut.sort((a, b) => a[0] - b[0]);
	console.log({treesToCut});

	let recurse = (startingPoint, nextTreeCoordinates) => {
		// BFS
		let pathSum = -1;
		let seen = new Map();
		let queue = [];
		queue.push(startingPoint);

		while (queue.length > 0) {
			pathSum++;
			// level order traversal
			let size = queue.length;
			while (size-- > 0) {
				let [nextRow, nextColumn] = queue.shift();
				// base case
				if (nextRow == nextTreeCoordinates[0] && nextColumn == nextTreeCoordinates[1])
					return pathSum;

				// can we get to nextTreeToCut from here?
				for (var i = 0; i < dr.length; i++) {
					let nr = nextRow + dr[i];
					let nc = nextColumn + dc[i];
					if (
						nr < 0 ||
						nr >= forest.length ||
						nc < 0 ||
						nc >= forest[0].length ||
						forest[nr][nc] == 0 ||
						seen.has(`${nr},${nc}`)
					)
						continue;
					queue.push([nr, nc]);
					seen.set(`${nr},${nc}`, true);
				}
				seen.set(`${nextRow},${nextColumn}`, true);
			}
		}

		return -1;
	};

	let pathSum = 0;
	let startingPoint = [0, 0];
	while (treesToCut.length > 0) {
		let [nextTreeHeight, nextTreeCoordinates] = treesToCut.shift();

		let sumToNext = recurse(startingPoint, nextTreeCoordinates);
		// maybe we can't get to the next location
		if (sumToNext == -1) return -1;
		pathSum += sumToNext;
		startingPoint = nextTreeCoordinates;
	}

	return pathSum;
};

let forest = [
	[1, 2, 3],
	[0, 0, 4],
	[7, 6, 5],
];
forest = [[1,2,3],[0,0,0],[7,6,5]];
forest = [[2,3,4],[0,0,5],[8,7,6]];
console.log(cutOffTree(forest));
