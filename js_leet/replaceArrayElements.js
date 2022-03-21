// Given an array arr, replace every element in that array with the greatest element among the elements to its right,
// and replace the last element with -1.

// After doing so, return the array.

// Input: arr = [17,18,5,4,6,1]
// Output: [18,6,6,6,1,-1]
// Explanation:
// - index 0 --> the greatest element to the right of index 0 is index 1 (18).
// - index 1 --> the greatest element to the right of index 1 is index 4 (6).
// - index 2 --> the greatest element to the right of index 2 is index 4 (6).
// - index 3 --> the greatest element to the right of index 3 is index 4 (6).
// - index 4 --> the greatest element to the right of index 4 is index 5 (1).
// - index 5 --> there are no elements to the right of index 5, so we put -1.

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function (arr) {
	// okay, we should probably start at the end and work towards the start
	let maxNumberToRight = -1;

	for (var i = arr.length - 1; i >= 0; i--) {
		// either we're bigger than the existing max, or not
		let nextMax = Math.max(maxNumberToRight, arr[i]);
		// replace us
		arr[i] = maxNumberToRight;
		maxNumberToRight = nextMax;
	}
	return arr;
};

let arr = [17, 18, 5, 4, 6, 1];
arr = [400];
console.log(replaceElements(arr));
