# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = []
        m = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                '8':['t','u','v'], '9':['w','x','y','z']}

        # letters
        for c in digits:
            if len(l) == 0:
                for ltr in m[c]:
                    l.append(ltr)
            else:
                nl = []
                tmp = l[:]
                # map letters
    
                for ltr in m[c]:
                    ntmp = tmp[:]
                    # dictionary as is...
                    for i in range(len(ntmp)):
                        ntmp[i] += ltr
                        print(ntmp[i])
                    nl += ntmp
                l = nl
        return l
if __name__ == "__main__":
    s = "23"
    sl = Solution()
    print(sl.letterCombinations(s))

