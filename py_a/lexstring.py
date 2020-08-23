# Return the lexicographically smallest subsequence of text that 
# contains all the distinct characters of text exactly once.

# Input: "cdadabcc"
# Output: "adbc"
from collections import Counter
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        s = ""
        c = Counter(text)
        print(c.keys())

        return s


if __name__ == "__main__":
    s = "cdadabcc"
    sol = Solution()
    print(sol.smallestSubsequence(s))