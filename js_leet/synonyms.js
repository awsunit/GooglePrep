// /**
//  * @param {string[][]} synonyms
//  * @param {string} text
//  * @return {string[]}
//  */
//  var generateSentences = function(synonyms, text) {
//     // go through the text
//     // everytime we find a word with a synonym:
//     //  create two separate sentences and recurces on those

//     // create a map??
//     let synonymMap = createMap(synonyms);


//     let splitWords = text.split(' ');
//     let equivalentStrings = recurse(splitWords, synonymMap);

//     equivalentStrings.sort();

//     console.log({equivalentStrings});
//     return equivalentStrings;

// };

// var createMap = (synonyms) => {
//     let finalMap = new Map();

//     synonyms.forEach((tuple) => {
//         // console.log({t0: tuple[0], t1:tuple[1]});
//         let word = tuple[0], synonym = tuple[1];

//         let wordMap = finalMap.has(word) ? finalMap.get(word) : {};
//         let synonymMap = finalMap.has(synonym) ? finalMap.get(synonym) : {};
//         wordMap[synonym] = true;
//         wordMap[word] = true;
//         Object.keys(wordMap).forEach((w) => {
//             synonymMap[w] = true;
//         });
//         Object.keys(synonymMap).forEach((w) => {
//             wordMap[w] = true;
//         });

//         finalMap.set(word, wordMap).set(synonym, synonymMap);

//         let seenWords = {};
//         let stack = [];
//         stack.push(word, synonym);

//         while (stack.length > 0) {
//             let poppedWord = stack.shift();
//             if (!seenWords[poppedWord]) {
//                 let poppedWordSynonyms = finalMap.get(poppedWord);
//                 Object.keys(poppedWordSynonyms).forEach((w) => stack.push(w));
//                 // add both word and synonym
//                 poppedWordSynonyms[word] = true;
//                 poppedWordSynonyms[synonym] = true;
//                 finalMap.set(poppedWord, poppedWordSynonyms);
//                 seenWords[poppedWord] = true;
//             }
//         }

//     });
//     // finalMap.forEach((value, key) => {
//     //     console.log(value);
//     // });
//     return finalMap;
// }

// var recurse = function(splitWords, synonymMap) {
//     // start with an empty string
//     let sentences = [''];

//     splitWords.forEach((word) => {
//         // console.log(word);
//         if (synonymMap.has(word)) {
// 			console.log('here');
//             // bifurcate
//             let synonyms = synonymMap.get(word);

//             let copiesOfSentences = [];

//             Object.keys(synonyms).forEach((synonym) => {
//                 let copyOfSentences = [...sentences];
//                 copyOfSentences = copyOfSentences.map((sentence) => sentence + ` ${synonym}`);
//                 copyOfSentences.forEach((copy) => copiesOfSentences.push(copy));
//             })
//             sentences = copiesOfSentences;
//         } else {
//             sentences = sentences.map((sentence) => {
//                 return sentence + ` ${word}`;
//             })
//         }
//     })
//     sentences = sentences.map((sentance) => sentance.trim());
//     return sentences;
// }

/**
 * @param {string[][]} synonyms
 * @param {string} text
 * @return {string[]}
 */
 var generateSentences = function(synonyms, text) {
    // go through the text
    // everytime we find a word with a synonym:
    //  create two separate sentences and recurces on those

    // create a map??
    let synonymMap = createMap(synonyms);


    let splitWords = text.split(' ');
    let equivalentStrings = recurse(splitWords, synonymMap);

    equivalentStrings.sort();

    // console.log({equivalentStrings});
    return equivalentStrings;

};

function createMap(synonyms) {
    // create a list of lists
    let lists = [[]];

    synonyms.forEach((tuple) => {
        let word = tuple[0], synonym = tuple[1];
        //  see if there's a list that includes word
        let synonymList = lists.find((l_i) => {
            return l_i.includes(word);
        });
        if (!synonymList) {
            // siff if there's a list that includes the synonym
            synonymList = lists.find((l_i) => {
                return l_i.includes(synonym);
            })
        }
        if(!synonymList) {
            // no list existed, create one
            lists.push([word, synonym]);
        } else {
            // append word || synonym
            if (!synonymList.includes(word)) synonymList.push(word);
            if (!synonymList.includes(synonym)) synonymList.push(synonym);
        }


    });
    let finalLists = [];
    lists.forEach((synonymList) => {
        // merge any common lists
        synonymList.forEach((word) => {
            finalLists.forEach((existingList) => {
                if (existingList.includes(word)) {
                    // merge these two lists

                }
            })
        })

    })
    console.log(lists);
    return lists;
}

// // let synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]];
// // let sentence = "I am happy today but was sad yesterday";
let synonyms = [["a","b"],["b","c"],["d","e"],["c","d"]];
let sentence = "a b";

generateSentences(synonyms, sentence);