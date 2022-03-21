// Given a string paragraph and a string array of the banned words banned,
// return the most frequent word that is not banned.
// It is guaranteed there is at least one word that is not banned, and that the answer is unique.

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
	// obviously a map with counts
	let wordOccurrences = new Map();
	let charactersToRemoveRegex = /[^a-zA-Z]/
	let splitWords = paragraph.split(charactersToRemoveRegex);

	// we actually need to regex this...
	splitWords.map((wordWithPunctuation) => {
		let updatedWord = wordWithPunctuation.replace(charactersToRemoveRegex,"").toLowerCase();
		if (!updatedWord) return '';
		if (wordOccurrences.has(updatedWord)) {
			wordOccurrences.set(updatedWord, wordOccurrences.get(updatedWord) + 1);
		} else {
			wordOccurrences.set(updatedWord, 1);
		}
		// console.log({updatedWord});
		return updatedWord;
	});

	// okay remove any banned word
	banned.forEach((bannedWord) => {
		wordOccurrences.delete(bannedWord);
	});

	// sort, than return the word which occurred the most
	let kv = {k: 'initV', v: 0};

	wordOccurrences.forEach((v,k) => {
		if (v > kv.v) {
			kv.k = k;
			kv.v = v;
		}
	})

	return kv.k;

};

let paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"];
paragraph = "a.", banned = [];
// paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"];


console.log(mostCommonWord(paragraph, banned));