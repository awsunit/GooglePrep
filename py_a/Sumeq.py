class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        l = self.fillr(root)
        l = sorted(l)
        spot = 0
        while spot < len(l) - 1:
            if l[spot] > k:
                return False
            nxt = spot + 1
            while nxt < len(l):
                if l[nxt] > k:
                    break
                if l[spot] + l[nxt] == k:
                    return True
                nxt +=1
            spot += 1

    def fillr(self, root):
        if root is None:
            return []
        l = [root.val]
        l += self.fillr(root.right)
        l += self.fillr(root.left)
        return l

    
        