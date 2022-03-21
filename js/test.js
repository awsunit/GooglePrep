

let combos = [0,0,0];
let val = 1;
let times = 11;
// while (combos != [0,0,0]) {

const moreCombos = () => {
    // console.log(combos);
    let nonZero = combos.some((combo) => combo!=0);
    if (nonZero) return true;
    return false;
}



do {
    combos.reduce((prevVal, curVal, index) => {
        // console.log({prevVal}, {curVal}, {index}, {val: combos[index]});
        combos[index] += prevVal;
        if (combos[index] == 10) {
            combos[index] = 0;
            return 1;
        } else {
            return 0;
        }

    }, 1);
    console.log({combos});
    times--;
} while (moreCombos());

console.log('done');