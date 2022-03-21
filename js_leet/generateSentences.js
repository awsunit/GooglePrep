/**
 * @param {string[][]} synonyms
 * @param {string} text
 * @return {string[]}
 */
 var generateSentences = function(synonyms, text) {
    
    // all possible sentences
    let synonymMap = new Map();
    
    synonyms.forEach(([firstWord, secondWord]) => {
        synonymMap.set(firstWord, secondWord);
        synonymMap.set(secondWord, firstWord);
    });
    
    // ez
    let splitText = text.split(' ');
    // loop through text
    // for every word that has a synonym, create a new string with us replaced
    
    let sentences = [text];
    let seenSentences = new Map();
    let result = [];
    while (sentences.length > 0) {
        let nextSentence = sentences.shift();
        seenSentences.set(nextSentence, true);
        result.push(nextSentence);
        
        let split = nextSentence.split(" ");
        for (var i = 0; i < split.length;i++) {
            let word = split[i];
            if (synonymMap.has(word)) {
                let synonym = synonymMap.get(word);
                // create new sentence
                let newSentence = split.reduce((s, nextWord, s_i) => {
                    if (s_i == i) {
                        return s + ` ${synonym}`;
                    } else {     
                        return s + ` ${nextWord}`;
                    }
                }, '');
                console.log({newSentence});
                if (!seenSentences.has(newSentence)) {
                    sentences.push(newSentence);
                    seenSentences.set(newSentence, true);
                } else {
                    // we've been here before, no need to append us
                }
            
            } else {
                // no synonym to worry about
            }
        }

    }
    return result;  
};

let synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday";