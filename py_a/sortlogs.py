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

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # () () ()
        l = []
        for i in range(n):
            l.append("(")
            l.append(")")

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return []

        # 'make' two lists
        # pointer to front - 1 -> beginning of letters
        # pointer to len() -> beginning of digits
        # while pl < pr:
        #     if pl + 1 not string only
        #         pr = pr - 1
        #         swap with pr
        #     else:
        #         place it in sorted position
        #         t = pl
        #         while t > 0:
        #           if cur > @t
        #               this is the spot -> swap
                        # break
        #               t -= 1

        #         pl += 1  

        # go back through from digits and swap back to original order

        
        # seperate logs:
        # if the first word after id == digit -> digits

