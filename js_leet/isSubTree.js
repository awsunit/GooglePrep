// Given the roots of two binary trees root and subRoot,
// return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

// A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
// The tree tree could also be considered as a subtree of itself.

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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
 var isSubtree = function(root, subRoot) {

	// what are the conditions of this being true
	// 1. subRoot == some node, n, exists-in root
	// 2. n.left == subRoot.left && n.right == subRoot.right
	// the recursive steps also prove true

	// so recurse works on a single starting point of root
	// if a node of root returns false, try another until exhausted
	return firstRecurse(root, subRoot);

};

function firstRecurse(root, subRoot) {
    // console.log(root, subRoot);
    // what about one of them being undefined -> then not a subtree
	if ((!root && subRoot) || (!subRoot && root)) return false;
	// both undefined -> that's fine
	if (!root && !subRoot) return true;

	if (!recurse(root, subRoot)) {
        let left = firstRecurse(root.left, subRoot);
        let right = firstRecurse(root.right, subRoot);
        if (left || right) {
            // console.log('one was true')
            return true;
        }
        return false;
	} else {
		return true;
	}
}

function recurse(rootNode, subRootNode) {
    // console.log('a', rootNode, subRootNode);
	// what about one of them being undefined -> then not a subtree
	if ((!rootNode && subRootNode) || (!subRootNode && rootNode)) return false;
	// both undefined -> that's fine
	if (!rootNode && !subRootNode) return true;
	// our values don't match -> not a subtree
	if (rootNode.val != subRootNode.val) return false;

	// we are fine at this stage but we need our subtrees to also be correct
    let left = recurse(rootNode.left, subRootNode.left);
    let right = recurse(rootNode.right, subRootNode.right);
    // console.log({left: left, right: right});
    if(left && right) {
        // console.log('returning true')
        return true;
    }
    return false;
}