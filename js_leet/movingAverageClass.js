// Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

// Implement the MovingAverage class:

//     MovingAverage(int size) Initializes the object with the size of the window size.
//     double next(int val) Returns the moving average of the last size values of the stream.

// Input
// ["MovingAverage", "next", "next", "next", "next"]
// [[3], [1], [10], [3], [5]]
// Output
// [null, 1.0, 5.5, 4.66667, 6.0]


// Explanation
// MovingAverage movingAverage = new MovingAverage(3);
// movingAverage.next(1); // return 1.0 = 1 / 1
// movingAverage.next(10); // return 5.5 = (1 + 10) / 2
// movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
// movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

/**
 * @param {number} val
 * @return {number}
 */
let next = function(val) {
	this.arrayOfIntegers.push(val);
	if (this.arrayOfIntegers.length > this.size) {
		this.arrayOfIntegers.shift();
	}
	// is there a smarter way to calculate this?
	let average =  this.arrayOfIntegers.reduce((sum, val) =>  sum + val, 0)/this.arrayOfIntegers.length;
	// console.log({average});
	return average;

};

/**
 * @param {number} size
 */
 var MovingAverage = function(size) {
	// we need to return an object here
	return {arrayOfIntegers: [], size: size, next: next};
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */

let movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3