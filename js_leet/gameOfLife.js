// According to Wikipedia's article: "The Game of Life, also known simply as Life,
// is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

// The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
// Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

//     Any live cell with fewer than two live neighbors dies as if caused by under-population.
//     Any live cell with two or three live neighbors lives on to the next generation.
//     Any live cell with more than three live neighbors dies, as if by over-population.
//     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

// The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

// Given the current state of the m x n grid board, return the next state.


// Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
// Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

// up, down, right, left
let dr = [-1, 1, 0, 0];
let dc = [0, 0, 1, -1];

// tl, tr, bl, br
let ddr = [-1, -1, 1, 1];
let ddc = [-1, 1, -1, 1];

function getNumberOfAliveNeighbors(r_i, c_i, board) {
	let count = 0;
	// get all the neighbords

	// up, down, left, right
	for (var i = 0; i < dr.length; i++) {
		let row = r_i + dr[i];
		let column = c_i + dc[i];

		if (row < 0 || column < 0 || row >= board.length || column >= board[0].length) continue

		if (board[row][column] == 1) count += 1;
	}

	// tl, tr, bl, br
	for (var i = 0; i < ddr.length; i++) {
		let row = r_i + ddr[i];
		let column = c_i + ddc[i];

		if (row < 0 || column < 0 || row >= board.length || column >= board[0].length) continue

		if (board[row][column] == 1) count += 1;
	}

	return count;
}

/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
 var gameOfLife = function(board) {
    let nextBoardState = [];

	board.forEach((row) => nextBoardState.push([...row]));

	for (var r_i = 0;r_i < board.length;r_i++) {
	// board.forEach((row, r_i) => {
		// add another row into the state
		for (var c_i = 0;c_i < board[r_i].length;c_i++) {
		// row.forEach((columnValue, c_i) => {
			let aliveNeighborCount = getNumberOfAliveNeighbors(r_i, c_i, nextBoardState);
			if (board[r_i][c_i] == 0) {
				// this is dead
				if (aliveNeighborCount == 3) {
					board[r_i][c_i] = 1;
				} else {
					board[r_i][c_i] = 0;
				}
			} else {
				// this is alive
				if (aliveNeighborCount < 2) {
					board[r_i][c_i] = 0;
				} else if (aliveNeighborCount > 3) {
					board[r_i][c_i] = 0;
				} else {
					board[r_i][c_i] = 1;
				}
			}

		};
		console.log({nextRow});
	};

};

let board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]];
console.log(gameOfLife(board));