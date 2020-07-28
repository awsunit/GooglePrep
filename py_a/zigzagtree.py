from typing import List
from string import ascii_lowercase, ascii_uppercase
import itertools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        r = 1
        return self.zzlo(root, r)

    def zzlo(self, root, rorl):
        # tree's ALWAYS have a base
        # print("looking at root: ", root)

        if root is None:
            return []

        r = []
        r.append([root.val])
    
        left = self.zzlo(root.left, rorl ^ 1)
        right = self.zzlo(root.right, rorl ^ 1)
        # print("left", left)
        # print("right", right)

        mm = []
        q = list(itertools.zip_longest(left, right))
        for tpl1, tpl2 in q:
            tpl1 = [] if tpl1 is None else tpl1
            tpl2 = [] if tpl2 is None else tpl2
            if rorl:
                v = tpl2 + tpl1
            else:
                v = tpl1 + tpl2
            mm.append(v)
            rorl ^= 1
                # p(q)
     
        r += mm
        return r
        
                 
       




def buildTree(nodes, spot):
    if spot >= len(nodes):
        return None

    CUR = nodes[spot]

    if nodes[spot] == "null":
        # print("found none")
        return None

    n = TreeNode(nodes[spot])
    ls = 1 + (2*spot)
    rs = 2 + (2*spot)

    # print("spot {}, val {}, ls {}, rs{}".format(spot, nodes[spot], ls, rs))

    n.left = buildTree(nodes, ls)
    n.right = buildTree(nodes, rs)



    return n

def p(x):
    print(x)

if __name__ == "__main__":


    f = open("ls1.txt", "r")

    line = f.readline()
    print(line)
    mx = max(line)
    t = buildTree(line.split(","), 0)

    a = [[2],[4,5],[7]]
    b = [[3],[6],[8]]


    # z = list(itertools.zip_longest(a, b))
    # # zz = list(itertools.zip_longest(b,a))
    # p(z)
    # # r = []
    # rr = 1
    # # # tuples of lists of ints
    # for tpl1, tpl2 in z:
    #     tpl1 = [] if tpl1 is None  else tpl1
    #     tpl2 = [] if tpl2 is None else tpl2
    #     if rr:
    #         v = tpl2 + tpl1
    #     else:
    #         v = tpl1 + tpl2
    #     rr ^= 1
    #     print(v)



    # c =  [i for i in (list(p for p in pair if p is not None)
    #         for pair in c)]
    # # c = list(filter(lambda tpl: None in tpl, c ))
    # print(c)



    s = Solution()
    r = []
    r = s.zigzagLevelOrder(t)

    for l in r:
        print(l)