// Given a list of dominoes,
// dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
// if and only if either (a == c and b == d), or (a == d and b == c) -
// that is, one domino can be rotated to be equal to another domino.

// Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

// Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
// Output: 1

/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function (dominoes) {
	let foundPairs = 0;
	for (var currentDomino = 0; currentDomino < dominoes.length; currentDomino++) {
		let domino = dominoes[currentDomino];
		for (var nextDomino = currentDomino + 1; nextDomino < dominoes.length; nextDomino++) {
			let dominoToCompare = dominoes[nextDomino];
			if (
				(domino[0] == dominoToCompare[0] && domino[1] == dominoToCompare[1]) ||
				(domino[0] == dominoToCompare[1] && domino[1] == dominoToCompare[0])
			) {
				foundPairs++;
			}
		}
	}
	return foundPairs;
};
let dominoes = [
	[1, 2],
	[2, 1],
	[3, 4],
	[5, 6],
];
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]];
console.log(numEquivDominoPairs(dominoes));
