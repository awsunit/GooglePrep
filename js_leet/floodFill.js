// An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

// You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

// To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

// Return the modified image after performing the flood fill.



let dr = [-1,1,0,0];
let dc = [0,0,-1,1];

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {

    // okay okay
    // we essentially keep looping until we can't flood another color
    let colorToChange = image[sr][sc];
    let indicesToFlood = [[sr, sc]];
    let seen = new Map();
    while (indicesToFlood.length > 0) {
        let [row, column] = indicesToFlood.pop();
        // console.log({row, column})
        let newKey = `${row},${column}`;
        if (seen.has(newKey)) continue;

        for (var i = 0; i < dr.length; i++) {
            let nr = row + dr[i];
            let nc = column + dc[i];
            // console.log({nr, nc})
            let nk = `${nr},${nc}`;
            if (nr < 0 || nr >= image.length || nc < 0 || nc >= image[0].length || seen.has(nk) || image[nr][nc] != colorToChange) continue;
            // console.log(image[nr][nc], {nr, nc});
            indicesToFlood.push([nr,nc]);
            // image[nr][nc] = newColor;
            // seen.set(nk, true);
        }

        image[row][column] = newColor;
        seen.set(newKey, true);
    }

    return image;

};

// let image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2;
// console.log(floodFill(image, sr, sc, newColor));