/**
 * @param {number} n
 * @return {number[][]}
 */
 var generateMatrix = function(n) {
    let result = [];
    for (var r = 0;r < n;r++) {
        let newRow = [];
        for (var c = 0;c < n;c++) {
            newRow.push(0);
        }
        result.push(newRow);
    }

    let tb = 0, bb = n-1, lb = 0, rb = n-1;

    let currentRow = 0, currentColumn = 0;

    let currentNumber = 1;

    while (true) {
        // go right
        for (var c = lb;c <= rb;c++) {
            result[tb][c] = currentNumber++;
        }
        // go down, plus 1 since we just did the tb row
        for (var r = tb + 1;r <= bb;r++) {
            result[r][rb] = currentNumber++;
        }

        // go left, minus one since we just did rb on this row
        for (var c = rb - 1;c >=lb;c--) {
            result[bb][c] = currentNumber++;
        }

        // go up, minues one since we just did this row, and we already did the top row
        for (var r = bb - 1;r >=tb+1;r--) {
            result[r][lb] = currentNumber++;
        }

        tb += 1;
        bb -= 1;
        lb += 1;
        rb -= 1;

        if (lb > rb && tb > bb) return result;
    }

};

let a = [2,2,2];

a.reduce((sum, curre))