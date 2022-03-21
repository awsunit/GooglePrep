// Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

// If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters,
//  reverse the first k characters and leave the other as original.

// Input: s = "abcdefg", k = 2
// Output: "bacdfeg"

// Input: s = "abcd", k = 2
// Output: "bacd"

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
 var reverseStr = function(s, k) {
	// okay okay
	// sliding window
	let currentWindow = 0; // incremements by 2k in loop
	let newString = '';
	while (currentWindow < s.length) {
		// get our window
		let rightIndex = currentWindow + (2 * k);
		// we don't want to go out of bound here
		rightIndex = rightIndex >= s.length ? s.length : rightIndex;
		// substring
		let substring = s.substring(currentWindow, rightIndex);
		// get the k amount of characters
		let characterToGrab = k > substring.length ? substring.length : k;
		// reverse as needed
		let reversed = substring.substring(0, characterToGrab).split("").reverse().join("");
		// create the new string
		newString += reversed + substring.substring(characterToGrab);
		// console.log({newString});

		// update currentWindow
		currentWindow += 2 * k;
	}

	return newString;

};

let s = "abcdefg", k = 2;

s = "abcd", k = 2;

console.log(reverseStr(s, k));