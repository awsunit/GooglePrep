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
	// n logn
	// look at possibly every node on root1
	// run binary seach on root2 for target value

	return recurseOnFirstTree(root1, root2, target);

};

// always starts with the root of second tree
// works through all nodes of first tree
function recurseOnFirstTree(firstTreeNode, secondTreeRoot, target) {
   console.log(firstTreeNode, secondTreeRoot);
   if (!firstTreeNode || !secondTreeRoot) return false;

   // how's the value compare
   let summation = firstTreeNode.val + secondTreeRoot.val;
   if (summation == target) {
	   console.log('firsttree true', firstTreeNode, secondTreeRoot);
	   return true;

   }

   // okay summation was either too big or too small
   if (summation > target) {
	   // look at left side of secondTree
	   let leftSideHadMatch = recurseOnSecondTree(firstTreeNode, secondTreeRoot.left, target);
	   if (leftSideHadMatch) return true;
   } else {
	   // summation < target
	   // look at right side of secondTree
	   let rightSideHadMatch = recurseOnSecondTree(firstTreeNode, secondTreeRoot.right, target);
	   if (rightSideHadMatch) return true;
   }
   return recurseOnFirstTree(firstTreeNode.left, secondTreeRoot, target) || recurseOnFirstTree(firstTreeNode.right, secondTreeRoot, target);

}

// we keep firstTreeNode as constant
// work through all all nodes of secondTree
function recurseOnSecondTree(firstTreeNode, secondTreeNode, target) {
   console.log(firstTreeNode, secondTreeNode);
   if (!firstTreeNode || !secondTreeNode) return false;

   let summation = firstTreeNode.val + secondTreeNode.val;

   if (summation == target) {
	   console.log('summed true', firstTreeNode, secondTreeNode);
	   return true;
   }

   if (summation > target) {
	   // look at left side
	   let leftSideHadMatch = recurseOnSecondTree(firstTreeNode, secondTreeNode.left, target);
	   if (leftSideHadMatch) return true;
   } else {
	   // summation < target
	   // look at right side
	   let rightSideHadMatch = recurseOnSecondTree(firstTreeNode, secondTreeNode.right, target);
	   if (rightSideHadMatch) return true;
   }
   return false;
}



// [0,-10,10] [5,1,7,0,2]
// [0,-10,10] [7]
// [0,-10,10] null
// [-10] [5,1,7,0,2]
// [-10] [7]
// [-10] null
// null [5,1,7,0,2]
// null [5,1,7,0,2]
// [10] [5,1,7,0,2]
// [10] [7]
// [10] null
// null [5,1,7,0,2]
// null [5,1,7,0,2]

