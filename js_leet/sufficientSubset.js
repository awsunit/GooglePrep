// Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

// A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

// A leaf is a node with no children.


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
 * @param {number} limit
 * @return {TreeNode}
 */
 var sufficientSubset = function(root, limit) {
    if (!root) return null;

    return recurse(root,limit, 0);


};

function recurse(node, limit, sumSoFar) {
    // if (!node) return null; NEVER GUNNA HAPPEN???

    // leaf is base case
    if (!node.left && !node.right) {
        sumSoFar += node.val;
        if (sumSoFar >= limit) {
            // we keep this leaf and path to leaf
            // console.log('good leaf', {node, limit, sumSoFar})
            return node;
        } else {
            // we need to delete this leaf and somehow communicate up to parent
            // console.log('bad leaf', {node, limit, sumSoFar})
            return null;
        }
    }

    // not at a leaf
    if (!node.left) {
        let newRight = recurse(node.right, limit, sumSoFar + node.val);
        node.right = newRight;
    } else if (!node.right) {
        let newLeft = recurse(node.left, limit, sumSoFar + node.val);
        node.left = newLeft;
    } else {
        // both
        let newLeft = recurse(node.left, limit, sumSoFar + node.val);
        let newRight = recurse(node.right, limit, sumSoFar + node.val);
        node.left = newLeft;
        node.right = newRight;
    }
    // console.log({node, left: node.left, right: node.right})

    // we started having children, but they've since been removed
    if (!node.right && !node.left) return null;

    return node;
}