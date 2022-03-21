/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
 var slowestKey = function(releaseTimes, keysPressed) {
    // okay, we need to track two things

    // updates
    let maxDuration = -1;
    // populates
    let keysWithMaxDuration = [];

    let splitKeys = keysPressed.split(""); // array

    splitKeys.forEach((k, k_i) => {
        if (k_i == 0) {
            // first key
            maxDuration = releaseTimes[0];
            keysWithMaxDuration.push(k);
        } else {
            let currentDuration = releaseTimes[k_i] - releaseTimes[k_i - 1];
            if (currentDuration > maxDuration) {
                maxDuration = currentDuration;
                keysWithMaxDuration = [k];
            } else if (currentDuration == maxDuration) {
                keysWithMaxDuration.push(k);
            } else {
            }
        }
    });
    // sort descending, grab first value
    keysWithMaxDuration = keysWithMaxDuration.sort((a,b) => b.localeCompare(a));
    return keysWithMaxDuration[0];

};