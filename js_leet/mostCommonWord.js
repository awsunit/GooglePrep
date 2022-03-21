// Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

// The words in paragraph are case-insensitive and the answer should be returned in lowercase.

// Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
// Output: "ball"
// Explanation:
// "hit" occurs 3 times, but it is a banned word.
// "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
// Note that words in the paragraph are not case sensitive,
// that punctuation is ignored (even if adjacent to words, such as "ball,"),
// and that "hit" isn't the answer even though it occurs more because it is banned.


/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
 var mostCommonWord = function(paragraph, banned) {
	 // first, count 'em up

	 let countMap = new Map();
	 let reg = /[^a-zA-Z]/;
	 let splitWords = paragraph.split(reg);
	//  console.log({splitWords});

	 splitWords.forEach((word) => {
		let cleanedWord = word.replace(reg, '').toLowerCase();
		if (cleanedWord) {
			countMap.set(cleanedWord, (countMap.get(cleanedWord) || 0) + 1);
		}
	 });
	 banned.forEach((bannedWord) => {
		 bannedWord = bannedWord.toLowerCase();
		 countMap.delete(bannedWord);
	 });
	 let entries = [];
	 countMap.forEach((v,k) => {
		 entries.push([v,k]);
	 });
	//  console.log(entries);
	 entries = entries.sort((a,b) => b[0] - a[0]);
	 return entries[0][1];

};

let paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"];
// paragraph = "a.", banned = [];
console.log(mostCommonWord(paragraph, banned));