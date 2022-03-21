// A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

//     Every adjacent pair of words differs by a single letter.
//     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
//     sk == endWord

// Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



// Example 1:

// Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
// Output: 5
// Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.







/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
 var ladderLength = function(beginWord, endWord, wordList) {
    // okay, okay
    // we are looking for a shortest path, sounds like BFS
    // we continually change the target node
    // we want to do a level-order search


    // base case
    if (!wordList.includes(endWord)) {
        return 0;
    }

    // it might be nice if we included a map
    // key: word, exist in wordlist
    // value: list of words who differ by one letter from key
    let offByOne = mapList([...wordList, beginWord]);
    // possibly used to help prevent duplicated work, will look like "word1,word2"
    let seenWordCombos = new Map();

    let transformationSteps = 0;
    let queue = [];
    queue.push(beginWord);

    while (queue.length > 0) {
        transformationSteps++;

        // level-order traversal
        let itemsToRemove = queue.length;

        while (itemsToRemove-- > 0) {
            let currentWord = queue.shift();
            let nearbyWords = offByOne.get(currentWord);

            for (var i = 0; i < nearbyWords.length; i++) {
                let nearbyWord = nearbyWords[i];
                let newKey = `${currentWord},${nearbyWord}`;
                if (seenWordCombos.has(newKey)) continue;
                if (nearbyWord == endWord) return transformationSteps + 1;
                queue.push(nearbyWord);
                seenWordCombos.set(newKey, true);
            }
        }

    }
    return 0;

};

function mapList(wordList) {
    let offByOne = new Map();

    const testOffByOne = (word, innerWord) => {
        let alreadyOffByOne = false;
        for (var i = 0; i < word.length; i++) {
            if (word.charAt(i) == innerWord.charAt(i)) continue;

            if (alreadyOffByOne) return false;
            alreadyOffByOne = true;
        }
        return true;
    }

    wordList.forEach((word) => {
        let currentList = [];// never seen this word?
        wordList.forEach((innerWord) => {
            if (word != innerWord) {
                if (testOffByOne(word, innerWord)) currentList.push(innerWord);
            }


        });
        offByOne.set(word, currentList);
    });


    // offByOne.forEach((v,k)=> console.log({k:k,v:v}));
    return offByOne;
}