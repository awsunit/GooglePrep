from collections import Counter
from typing import List
from string import ascii_lowercase
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        # iterate through lists, building map of char to positions
        c2l = {c:[] for c in ascii_lowercase}

        r = 0
        for row in board:
            c = 0
            for col in row:
                c2l[col].append((r,c))
                c += 1
            r += 1

        
        c2l_removed = c2l.copy()
  

        
        # # # first element and its placement list
        firstletter = word[0]
        first_list = c2l[firstletter]

        substr = word[1:]

        # iterate over letter coords, remove from list
        for spot in first_list:
            c2l_removed = c2l.copy()
            c2l_removed[]
            for


            
        


x = ['a', 'a', 'b']
y = ['c', 'a', 'b']
s = Solution()
s.exist([x,y], "wwhy")
# cx = Counter(x)
# cy = Counter(y)
# print(cx)
# print(cy)

# n = cx + cy
# print(n)