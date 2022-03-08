// A dieter consumes calories[i] calories on the i-th day.

// Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k),
// they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

//	If T < lower, they performed poorly on their diet and lose 1 point;
//	If T > upper, they performed well on their diet and gain 1 point;
//	Otherwise, they performed normally and there is no change in points.

// Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.

// Note that the total points can be negative.

// 1 <= k <= calories.length <= 10^5
// 0 <= calories[i] <= 20000
// 0 <= lower <= upper

/**
 * @param {number[]} calories
 * @param {number} k
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var dietPlanPerformance = function (calories, k, lower, upper) {
	// this is a sliding window problem
	// window is k
	let score = 0;

	// get first window
	let currentWindow = calories.slice(0, k);
	let currentWindowCalories = currentWindow.reduce((currentSum, calorieAmount) => {
		return currentSum + calorieAmount;
	}, 0);
	if (currentWindowCalories < lower) {
		score-=1;
	} else if (currentWindowCalories > upper) {
		score+=1;
	}

	for (let spot = k; spot < calories.length; spot++) {
		let caloriesToRemoveFromWindow = calories[spot-k];
		let caloriesToAddToWindow = calories[spot];
		currentWindowCalories-=caloriesToRemoveFromWindow;
		currentWindowCalories+=caloriesToAddToWindow;

		if (currentWindowCalories < lower) {
			score-=1;
		} else if (currentWindowCalories > upper) {
			score+=1;
		}
	}

	return score;
};

let calories = [6,5,0,0], k = 2, lower = 1, upper = 5

console.log(dietPlanPerformance(calories, k, lower, upper));
