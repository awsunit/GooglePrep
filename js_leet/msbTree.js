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
 var sumRootToLeaf = function(root) {
	// create an array, at leaf, calculate sum
	if (!root) return 0;
	Math.pow(0, 2);
	return recurse(root, []);

};

function recurse(root, oldListOfValues) {
  // if (!root) return calculateSum(listOfValues);

  let listOfValues = [...oldListOfValues];
  listOfValues.push(root.val);

  if (!root.left && !root.right) {
	  // console.log('neight');
	  return calculateSum(listOfValues);
  }
  if (!root.left) {
	  // console.log('has right');
	  return recurse(root.right, listOfValues);
  } else if(!root.right) {
	  // console.log('has left');
	  return recurse(root.left, listOfValues);
  } else {
	  // console.log('both');
	  return recurse(root.left, listOfValues) + recurse(root.right, listOfValues);
  }
}

function calculateSum(listOfValues) {
   // looks like [1,0,1,0]
//    console.log('calc', {listOfValues});
   let powerOfTwo = listOfValues.length - 1;
   let sum = listOfValues.reduce((sum, value) => {
	   let additional = value * Math.pow(2, powerOfTwo);
	//    console.log(sum, value, powerOfTwo, additional);
	   sum += additional;
	   powerOfTwo--;
	   return sum;
   }, 0);
//    console.log({sum});
   return sum;
}