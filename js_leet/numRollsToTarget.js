// You have n dice and each die has k faces numbered from 1 to k.

// Given three integers n, k, and target,
// return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target.

// Since the answer may be too large, return it modulo 10^9 + 7.

// Input: n = 1, k = 6, target = 3
// Output: 1
// Explanation: You throw one die with 6 faces.
// There is only one way to get a sum of 3.
/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
 var numRollsToTarget = function(n, k, target) {

    // okay, so we roll k times, trying to find target with those k rolls

    let memo = new Map();

    let md = 1000000007;

    let dp = (numberOfDice, target) => {
        if (numberOfDice == 0 || target < 0) {
            // console.log('breaking')
            return 0;
        }
        // subproblem
        // given the numberOfDice, how many ways can I reach target
        let nextKey = `${numberOfDice},${target}`;
        // console.log({nextKey});

        // base case -> we've been here before
        if (memo.has(nextKey)) {
            return memo.get(nextKey);
        }

        // base case -> one dice
        if (numberOfDice == 1) {
            // console.log('here')
            let count = 0;
            // we need to match the target
            if (target <= k && target >= 1) {
                count++;
            }
            // there's only one way to hit things here
            memo.set(nextKey, count);
            // console.log({count, target, k})
            return count;
        }

        // else, we need to recurse
        let waysToReachTarget = 0;
        for (var currentSide = 1;currentSide <= k;currentSide++) {
            // waysToReachTarget = waysToReachTarget % MD;
            let nextTarget = target - currentSide;
            let ways = dp(numberOfDice - 1, nextTarget)%md;
            waysToReachTarget+=ways;
            waysToReachTarget = waysToReachTarget%md;
        }


        // console.log({waysToReachTarget})
        waysToReachTarget = waysToReachTarget%md;
        memo.set(nextKey, waysToReachTarget);
        return waysToReachTarget;

    }
    let r = dp(n, target)%md;
    // console.log(isNaN(r));
    return r;

};

// let  n = 2, k = 6, target = 7;
// n = 30, k = 30, target = 500;
// console.log(numRollsToTarget(n,k,target));