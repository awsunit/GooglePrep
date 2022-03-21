// You have a queue of integers, you need to retrieve the first unique integer in the queue.

// Implement the FirstUnique class:

//     FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
//     int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
//     void add(int value) insert value to the queue.

// 	Input:
// ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
// [[[2,3,5]],[],[5],[],[2],[],[3],[]]
// Output:
// [null,2,null,2,null,3,null,-1]
// Explanation:
// FirstUnique firstUnique = new FirstUnique([2,3,5]);
// firstUnique.showFirstUnique(); // return 2
// firstUnique.add(5);            // the queue is now [2,3,5,5]
// firstUnique.showFirstUnique(); // return 2
// firstUnique.add(2);            // the queue is now [2,3,5,5,2]
// firstUnique.showFirstUnique(); // return 3
// firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
// firstUnique.showFirstUnique(); // return -1

/**
 * @param {number[]} nums
 */
 var FirstUnique = function(nums) {
	// do something with nums
	// map to counts?
	// create a holder index that we can always use?
	let countsMap = new Map();
	nums.forEach((num) => {
		countsMap.set(num, (countsMap.get(num) || 0) + 1);
	})
	let q = [...nums];
	let firstIndex = -1;
	for (var i = 0;i < nums.length;i++) {
		if (countsMap.get(nums[i]) == 1) {
			// first unique value
			firstIndex = i;
			break;
		}
	}
	return {queue: q, firstUniqueIndex: firstIndex, countsMap: countsMap, showFirstUnique: showFirstUnique, add:add};
};

/**
 * @return {number}
 */
let showFirstUnique = function() {
	// there doesn't exist any unique number right now
	if (this.firstUniqueIndex == -1) {
		console.log({firstUniqueIndex: -1});
		return this.firstUniqueIndex;
	}
	console.log({firstUniqueIndex: this.queue[this.firstUniqueIndex]});
	return this.queue[this.firstUniqueIndex];
};

/**
 * @param {number} value
 * @return {void}
 */
let add = function(value) {
	this.countsMap.set(value, (this.countsMap.get(value) || 0) + 1);
	this.queue.push(value);
	// this needs to update index
	let firstIndex = -1;
	for (var i = this.firstUniqueIndex;i < this.queue.length;i++) {
		if (this.countsMap.get(this.queue[i]) == 1) {
			// first unique value
			firstIndex = i;
			break;
		}
	}
	this.firstUniqueIndex = firstIndex;
	console.log('add', this.queue);
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * var obj = new FirstUnique(nums)
 * var param_1 = obj.showFirstUnique()
 * obj.add(value)
 */

// let firstUnique = new FirstUnique([2,3,5]);
// firstUnique.showFirstUnique(); // return 2
// firstUnique.add(5);            // the queue is now [2,3,5,5]
// firstUnique.showFirstUnique(); // return 2
// firstUnique.add(2);            // the queue is now [2,3,5,5,2]
// firstUnique.showFirstUnique(); // return 3
// firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
// firstUnique.showFirstUnique(); // return -1

let firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17