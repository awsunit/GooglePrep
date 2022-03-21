// Given an array of integers arr, replace each element with its rank.

// The rank represents how large the element is. The rank has the following rules:

//     Rank is an integer starting from 1.
//     The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
//     Rank should be as small as possible.

// Input: arr = [40,10,20,30]
// Output: [4,1,2,3]


/**
 * @param {number[]} arr
 * @return {number[]}
 */
 var arrayRankTransform = function(arr) {
    // let's map a number to its index(s)
	let indexMap = new Map();

	arr.forEach((val, val_i) => {
		if (indexMap.has(val)) {
			let existingIndexes = indexMap.get(val);
			existingIndexes.push(val_i);
			indexMap.set(val, existingIndexes);
		} else {
			indexMap.set(val, [val_i]);
		}
	});

	// okay, sort the values into ascending order
	let allValues = [];
	indexMap.forEach((v,k) => allValues.push(k));
	allValues.sort((a,b) => a-b);

	let rank = 1;
	allValues.forEach((sortedValue) => {
		let indexesWithValue = indexMap.get(sortedValue);
		indexesWithValue.forEach((i) => {
			arr[i] = rank;
		});
		rank++;
	})

	return arr;
};




let arr = [40,10,20,30];
// arr = [100,100,100];

console.log(arrayRankTransform(arr));
