// Given the roots of two binary search trees, root1 and root2, 
// return true if and only if there is a node in the first tree and a node in the second tree 
// whose values sum up to a given integer target.


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @param {number} target
 * @return {boolean}
 */
 var twoSumBSTs = function(root1, root2, target) {
	// first, let's find the two-complement
	let complementNumbers = new Map();
	fillWithComplements(complementNumbers, target, root1);
	return findComplement(complementNumbers, root2);
};

function findComplement(complementNumbers, node) {
	if (!node) return false;

	if (complementNumbers.has(node.val)) return true;

	return findComplement(complementNumbers, node.left) || findComplement(complementNumbers, node.right);
}

function fillWithComplements(complementNumbers, target, node) {
	if (!node) return;

	let complement = target - node.val;
	complementNumbers.set(complement, true);
	fillWithComplements(complementNumbers, target, node.left);
	fillWithComplements(complementNumbers, target, node.right)
}