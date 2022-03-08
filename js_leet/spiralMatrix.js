// Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
let spiralMatrix = [[]];
/**
 * @param {number} n
 * @return {number[][]}
 */
 var generateMatrix = function(n) {
	// okay, okay
	// start at 0,0, go until 0, n-1
	// then we go 0,n-1 -> n-1, n-1
	// then we go n-1,n-1-> n-1, 0
	// then we go: n-1, 0 -> 1,0
	// then we go: 1,0 -> 1, n-1

	move('right', 0, 0, n);
};

function move(direction, currentRow, currentColumn, n, currentNumber) {
	if (currentNumber > Math.pow(n, 2)) {
		// what is terminating condition
		return spiralMatrix;
	}

	switch (direction) {
		case 'up': {
			let row = currentRow;
			// todo not always 0
			while (row <= 0 + currentRow) {
				spiralMatrix[row][currentColumn];
				row--;
				currentNumber++;
			}
			return move('right', currentRow, 1, n, currentNumber);
		}
			//
		case 'down': {
			let row = currentRow;
			// TODO - its not always n, computable from column?
			while (row < n - currentRow + 1) {
				spiralMatrix[row][currentColumn] = currentNumber;
				row++;
				currentNumber++;
			}
			// TODO not always n-1
			return move('left', n-currentRow, currentColumn - 1, n, currentNumber);
		}
		case 'right': {
			let column = currentColumn;
			while (column < n - currentRow) {
				spiralMatrix[currentRow][column] = currentNumber;
				column++;
				currentNumber++;
			}
			// todo: there is some sort of offset for column value (not always n-1) (computable from row?)
			return move('down', currentRow + 1, n-1-currentRow, currentNumber);
		}
		case 'left': {
			let column = currentColumn;
			// TODO not always 0
			while (column >= 0 - currentColumn + 1) {
				spiralMatrix[currentRow][column] = currentNumber;
				column--;
				currentNumber++;
			}
			return move('up', currentRow - 1, currentColumn, n, currentNumber);
		}
	}
}

let n = 3;

// Output: [[1,2,3],[8,9,4],[7,6,5]]
console.log(generateMatrix(n));