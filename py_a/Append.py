# Given a non-empty string 
# check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together. 

# You may assume the given string consists of lowercase English letters 
# only and its length will not exceed 10000.
import re
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        st = ""
        l = len(s)
        for i in range(l):
            st += s[i]
            n = l//len(st)
            nst = st*n
            print(nst)
            if nst == s:
                if st != s:
                    return True
                return False
        return False     

if __name__ == "__main__":
    s = "aba"
    sp = Solution()
    print(sp.repeatedSubstringPattern(s))