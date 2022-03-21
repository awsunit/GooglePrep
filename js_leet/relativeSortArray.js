// Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

// Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
// Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.



// Example 1:

// Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
// Output: [2,2,2,1,4,3,3,9,6,7,19]



/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
 var relativeSortArray = function(arr1, arr2) {
    // okay, okay

    let mapOfIndexes = new Map();

    arr2.forEach((val, v_i) => {
        mapOfIndexes.set(val, v_i);
    });

    // okay, we have the order of elements
    // reconstruct the array?

    let countsInArr1 = new Map();
    arr1.forEach((val) => {
        countsInArr1.set(val, (countsInArr1.get(val) || 0) + 1);
    });

    // okay we have the number of elements
    let newArray = [];

    let valsAndIndexes = [];
    mapOfIndexes.forEach((v, k) => {
        valsAndIndexes.push([k,v]);
    });

    valsAndIndexes.sort((a,b) => a[1] - b[1]);
    // console.log(valsAndIndexes);

    valsAndIndexes.forEach(([val, order]) => {
        let numToAdd = countsInArr1.get(val); // guaranteed to exist
        // console.log(val, numToAdd);
        while (numToAdd-- > 0) {
            newArray.push(val);
            countsInArr1.delete(val);
        }
    });

    // console.log(countsInArr1);
    // okay we need to take whatever is left, sort in ascending order and append
    let remaining = [];
    countsInArr1.forEach((v,k) => {
        while(v-- > 0) {
            remaining.push(k);
        }
    });
    remaining = remaining.sort((a,b) => a-b);
    // console.log(remaining);
    remaining.forEach((val) => {
        newArray.push(val);
    });

    // console.log(newArray);
    return newArray;

};

// let arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6];
// console.log(relativeSortArray(arr1, arr2));