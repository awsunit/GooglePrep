from functools import reduce
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we should work each square
        rm = {i:['1','2','3','4','5','6','7','8','9'] for i in range(9)}
        cm = {i:['1','2','3','4','5','6','7','8','9'] for i in range(9)}
        subm = {i:['1','2','3','4','5','6','7','8','9'] for i in range(9)}
        
        sb = 0
        for row in range(len(board)):
            for col in range(len(board)):
                v = board[row][col]
                if v == '.':
                    continue
                # need to check that fucking cube
                # ez ones
                if v in rm[row] and v in cm[col]:
                    j = int(col / 3)
                    if 0 <= row and row < 3:
                        j += 0
                    elif 3 <= row and row < 6:
                        j += 3
                    else:
                        j += 6
                    if v in subm[j]:
                        rm[row].remove(v)
                        cm[col].remove(v)
                        subm[j].remove(v)
                    else:
                        return False
                else:
                    return False
        return True
            
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        for x,y in m.items():
            if y == 1:
                return x


if __name__ == "__main__":
    l = [1,2,3,1,2]
    s = Solution()
    # print(s.singleNumber(l))

    l = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]
    
    l = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(s.isValidSudoku(l))
        