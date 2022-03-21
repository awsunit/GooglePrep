/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxSumBST = function (root) {
	if (!root) return 0;
	return Math.max(0, binarySum(root)[0]);
};


function binarySum(node) {
	// INV - node is never null

	if (!node.left && !node.right) {
		// at a leaf, which is by default a BST, return our value
		console.log(node, 'at leaf');
		return [node.val, true];
	}


	if ((node.left && node.left.val >= node.val) || (node.right && node.right.val <= node.val)) {
		console.log(node, 'not a binary tree');
		// we are not a binary seach tree ourselves, so we can't combine the sum from our right and left
		// best we can do is return the max from them
		let leftSum = [0,false],
			rightSum = [0,false];
		if (node.left) {
			leftSum = binarySum(node.left);
		}
		if (node.right) {
			rightSum = binarySum(node.right);
		}
		let mv = Math.max(leftSum[0], rightSum[0]);
		console.log({ ls: leftSum, rs: rightSum, returning: mv });
		return [mv, false];
	} else {
		// okay, so far we uphold the BST rules
		console.log(node, 'is binary tree');
		let leftSum = undefined,
			rightSum = undefined;

		// we've already checked that the BST condition is upheld
		if (node.left) {
			leftSum = binarySum(node.left);
		}
		// same for our right node
		if (node.right) {
			rightSum = binarySum(node.right);
		}

		// were both bst?
		if (leftSum && rightSum && leftSum[1] && rightSum[1]) {
			let s = node.val;
			if (rightSum[0] != -Infinity) {
				s += rightSum[0];
			}
			if (leftSum[0] != -Infinity) {
				s += leftSum[0];
			}
			// let s = node.val + rightSum[0] + leftSum[0];
			let mv = Math.max(s, rightSum[0], leftSum[0]);
			console.log(node, 'both children BST', { sum: mv });
			return [mv, true];
		} else {
			let mv = Math.max(leftSum ? leftSum[0] : 0, rightSum ? rightSum[0]: 0);
			console.log(node, 'both children not BST', { mv: mv });
			return [mv, false];
		}
	}

	//
}
