// There are N stones in a pond, each having a value Ai written on it. 

// A frog is at stone 1 and wants to reach stone N. 

// The frog can jump from a stone i to any stone j(j>i). 

// Let d be the length of subarray (i.e. j−i+1), then the energy required for the jump is (d⋅Ai)−Aj. 

// Find the minimum non-negative amount of energy required by the frog to reach the N-th stone.

// Note: It is possible that the total amount of energy required is negative, 
// in that case, you should print the minimum non-negative value (i.e. 0).


// bfs / dfs thingy

//

// The first line contains an integer T
// - the number of test cases. Then the test cases follow.
// The first line of each test case contains an integer N
// - the number of stones.
// The second line contains N
// integers denoting the numbers written on the stones.

const readline = require('readline');

const lineReader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = '';

lineReader.on('line', (data) => {
    console.log({data});
});

lineReader.on('SIGINT', () => {
    console.log('byee');
    process.exit();
})


// process.stdin.resume();
// process.stdin.setEncoding('utf8');







// 

// process.stdin.on('data', (data) => {
//     console.log({data});
//     input+=data;
// });

// process.on('SIGINT', () => {
//     let splitInput = input.split('\n');
//     let testCases = parseInt(splitInput.shift());

//     solve(testCases);
// });


// function solve(testCases) {
//     process.stdout.write('done');
//     for (let testCase = 1; testCase <= testCases; testCase++) {
//         console.log(testCase);
//     }
//     console.log('done');
// }