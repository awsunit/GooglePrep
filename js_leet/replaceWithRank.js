// Given an array of integers arr, replace each element with its rank.

// The rank represents how large the element is. The rank has the following rules:

//     Rank is an integer starting from 1.
//     The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
//     Rank should be as small as possible.


/**
 * @param {number[]} arr
 * @return {number[]}
 */
 var arrayRankTransform = function(arr) {
	// this is easiest with a sorted list (ascending order)
	// entry_first rank = 1
	// let's sort into a tuple, tuple[0] contains value, tuple[1] contains the index that value was at
	// could do a map where key = element, value = all indices value occurs at
	let countMap = new Map();

	arr.forEach((val, index) => {
		if (countMap.has(val)) {
			let oldList = countMap.get(val);
			oldList.push(index);
			countMap.set(val, oldList);
		} else {
			countMap.set(val, [index]);
		}
	});

	// countMap.forEach((v,k) => console.log({k: k, v: v}));

	let sorted = [...countMap.entries()].sort((a, b) => a[0] - b[0]);
	// console.log({sorted});

	// repopulate
	let rank = 1;
	sorted.forEach((val) => {
		let locations = val[1];
		// console.log(locations);
		locations.forEach((location) => {
			arr[location] = rank;
		})
		rank++;
	})

	// console.log({arr});
	return arr;
};

let arr = [40,10,20,30];
arr = [100,100,100];
arr = [37,12,28,9,100,56,80,5,12];
console.log(arrayRankTransform(arr));