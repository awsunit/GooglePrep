/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
 var numKLenSubstrNoRepeats = function(s, k) {
    if (k > s.length) return 0;



    let start = 0;
    let numberOfSubstrings = 0;
    let countsMap = new Map();

    // let's get our first window
    let currentSubstring = s.substring(start, k);

    // let's get our counts
    let split = currentSubstring.split("");
    split.forEach((letter) => {
        countsMap.set(letter, (countsMap.get(letter) || 0) + 1);
    });

    let allUnique = true;
    countsMap.forEach((count,letter) => {
        if (count > 1) allUnique = false;
    });
    if (allUnique) numberOfSubstrings += 1;

    for (var i = k; i < s.length; i++) {
        let nextLetter = s.charAt(i);
        let letterToRemove = s.charAt(i - k);
        countsMap.set(letterToRemove, countsMap.get(letterToRemove) - 1);
        countsMap.set(nextLetter, (countsMap.get(nextLetter) || 0) + 1);

        let allUnique = true;
        countsMap.forEach((count,letter) => {
            if (count > 1) allUnique = false;
        });
        if (allUnique) numberOfSubstrings += 1;
    }


    return numberOfSubstrings;

};