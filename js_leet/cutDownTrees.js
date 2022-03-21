// You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

//     0 means the cell cannot be walked through.
//     1 represents an empty cell that can be walked through.
//     A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.

// In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

// You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

// Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

// You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

// Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
// Output: 6
// Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
let globalForest = undefined;
const UNABLE_TO_COMPLETE = -1;

// creating a left, right, top, bottom
// remember: x is actually the column and y is the row
let dx = [-1, 1, 0, 0];
let dy = [0, 0, 1, -1];
function sortForest(forest) {
	let sortedForest = [];

	forest.forEach((rowOfTrees, row_i) => {
		rowOfTrees.forEach((treeHeight, column_i) => {
			if (treeHeight > 1) {
				sortedForest.push([treeHeight, [row_i, column_i]]);
			}
		});
	});
	sortedForest.sort((a, b) => b[0] - a[0]);
	// console.log({sortedForest});
	return sortedForest;
}

function bfs(currentCoordinates, targetTreeCoordinates, stepsSoFar) {
	let queue = [];

	// map of coords to boolean
	let seen = new Map();
	queue.push(currentCoordinates);

	let steps = -1;

	while (queue.length > 0) {
		steps++;

		// okay, to ensure that we do level-order traversal
		// we look at all currently existing queue members BUT NOT THE ONES WE APPEND IN THE LOOP BELOW
		let currentQueueSize = queue.length;
		while (currentQueueSize-- > 0) {
			let [currentRow, currentColumn] = queue.shift();

			let mapKey = `${currentRow},${currentColumn}`;

			// don't look at nodes we have visited
			if (seen.has(mapKey)) continue;
			// update
			seen.set(mapKey, true);

			//we have a restriction that we can't walk through a spot with a value of 0
			if (globalForest[currentRow][currentColumn] == 0) continue;

			// is this the droid we are looking for?
			if (
				currentRow == targetTreeCoordinates[0] &&
				currentColumn == targetTreeCoordinates[1]
			) {
				return steps;
			}

			// else BFS
			for (var r = 0; r < dx.length; r++) {
				// x column, y is row
				let nextRow = currentRow + dx[r];
				let nextColumn = currentColumn + dy[r];
				let mapKey = `${nextRow},${nextColumn}`;
				// do we have the correct bounds, have we not seen this, is the node actuall passable
				if (
					nextRow < 0 ||
					nextColumn < 0 ||
					nextRow >= globalForest.length ||
					nextColumn >= globalForest[0].length ||
					seen.has(mapKey) ||
					globalForest[nextRow][nextColumn] == 0
				)
					continue;
				queue.push([nextRow, nextColumn]);
			}
		}
	}

	// if we end up in a state where the queue is empty, we haven't found a path
	return UNABLE_TO_COMPLETE;
}

/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function (forest) {
	// first we need to get the forest into an sorted structure so:
	// we can go from (0,0) to the shortest tree, then from the shortest tree to the next tallest, etc.
	let sortedForest = sortForest(forest);
	globalForest = forest;
	let currentCoordinates = [0, 0];
	let mininumNumberSteps = 0;
	while (sortedForest.length > 0) {
		let [nextTreeHeight, nextTreeCoordinates] = sortedForest.pop();

		// run BFS from currentLocation, looking for the shortest path to the next Tree
		let minimumStepsToNextTree = bfs(currentCoordinates, nextTreeCoordinates, 0);
		// maybe there was no existing path
		if (minimumStepsToNextTree == UNABLE_TO_COMPLETE) {
			return UNABLE_TO_COMPLETE;
		}
		mininumNumberSteps += minimumStepsToNextTree;
		// we will be starting from the next tree
		currentCoordinates = nextTreeCoordinates;
	}

	return mininumNumberSteps;
};

let forest = [
	[1, 2, 3],
	[0, 0, 4],
	[7, 6, 5],
];
// forest = [[1,2,3],[0,0,0],[7,6,5]];
forest = [
	[4, 2, 3],
	[0, 0, 1],
	[7, 6, 5],
]; // outputting 14, expecting 10
console.log(cutOffTree(forest));

// let newMap = new Map();
// // let newOb = {x:1,y:1};

// class Coord {
// 	constructor(row, column) {
// 		this.row = row;
// 		this.columm = column;
// 	}
// }
// let obj1 = new Coord(1,1);
// let obj2 = new Coord(1,1);

// // newMap.set({x:1,y:1},true);
// // newMap.set({x:1,y:1},true);
// newMap.set(obj1, true);
// newMap.set(obj2, true);

// newMap.forEach((v,k) => console.log({k:k,v:v}));
