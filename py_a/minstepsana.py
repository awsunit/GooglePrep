
# Given two equal-size strings s and t. 
# In one step you can choose any character of t and replace it 
# with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters 
# with a different (or the same) ordering.


# TRIVIAL IMPLEMENTATION

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        sun = []
        tun = []
        
        for c in range(len(s)):
            print(s[c], t[c])
            if s[c] != t[c]:
                if t[c] in sun:
                    sun.remove(t[c])
                    if s[c] in tun: # could swap
                        tun.remove(s[c])
                    else:
                        sun.append(s[c])
                elif s[c] in tun:
                    tun.remove(s[c])
                    tun.append(t[c])
                else:
                    sun.append(s[c])
                    tun.append(t[c])
                    
        count += len(sun) 
        print(sun, tun)
                
        return count
        


    

if __name__ == "__main__":
    s = Solution()
        
    print(s.minSteps("leetcode", "practice"))
    # print(s.minSteps("anagram", "mangaar"))