# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  

# It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  

# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
# The digit-logs should be put in their original order.

# Return the final order of the logs.
from typing import List
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # () () ()
        l = [""]
        for i in range(n):
            nl = []
            for li in l:
                sb1 = "(" + li + ")"
                sb2 = "()" + li
                nl.append(sb1)
                # base case of "()" "()"
                if sb1 != sb2:
                    nl.append(sb2)
            l = nl
        return l

if __name__ == "__main__":
    l = 3
    s = Solution()
    print(s.generateParenthesis(l))

    