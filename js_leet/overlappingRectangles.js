// An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], 
// where (x1, y1) is the coordinate of its bottom-left corner, 
// and (x2, y2) is the coordinate of its top-right corner. 

// Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

// Two rectangles overlap if the area of their intersection is positive. 

// To be clear, two rectangles that only touch at the corner or edges do not overlap.

// Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

// Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
// Output: true

/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
 var isRectangleOverlap = function(rec1, rec2) {

	// fill out double array?
	let width = Math.max(rec1[2], rec2[2]);
	let height = Math.max(rec1[3], rec2[3]);
	let arr = [];

	for (var row = 0; row < height; row++) {
		let newArr = [];
		for (var col=0; col < width;col++) {
			newArr.push(false);
		}
		arr.push(newArr);
	}

	for (var row = rec1[0]; row < height; row++) {
		for (var col=0; col < width;col++) {
		}
	}


};

function tryThis(r1, r2) {
	return r1[3] > r2[1] && r1[1] <= r2[1] && r1[2] > r2[0] && r1[0] <= r1[0];
}


let rec1 = [0,0,2,2], rec2 = [1,1,3,3];

console.log(isRectangleOverlap(rec1, rec2));