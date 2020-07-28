# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def parse(root, level, val, levelmax, levelmin):
    if root is None:
            return
        
    # add self to max and min
    if level not in levelmax:
        levelmax[level] = val

    if level not in levelmin:
        levelmin[level] = val

    if levelmax[level] < val:
        # furthest east
        levelmax[level] = val

    if levelmin[level] > val:
        # furthest west
        levelmin[level] = val

    lcv = val * 2
    rcv = lcv + 1

    parse(root.left, level + 1, lcv, levelmax, levelmin)
    parse(root.right, level + 1, rcv, levelmax, levelmin)

        

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        level = 1
        val = 1
        levelmin = {1:1}
        levelmax = {1:1}
        parse(root, level, val, levelmax, levelmin)

        result = {key: levelmax.get(key, 0) - levelmin.get(key, 0)
                    for key in set(levelmax) | set(levelmin)}
        return max(result.values())


# levelmin = {'a':2,'b':3,'c':4}
# m = max(levelmin.values())
# print("lowest: ", m)
# levelmax = {'a':4,'b':5,'c':5}

# result = {key: levelmax.get(key, 0) - levelmin.get(key, 0)
#                     for key in set(levelmax) | set(levelmin)}
# for r in result:
#     print(r, result[r])

