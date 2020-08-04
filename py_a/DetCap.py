# Given a word, you need to judge whether the usage of capitals in it
# is right or not.

# We define the usage of capitals in a word to be right when one 
# of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".

# Otherwise, we define that this word doesn't use capitals in a 
# right way.

import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        p = re.compile('^[a-z]+$')
        m = p.match(word)
        if m:
            print(m.group())
            print("a-z")
            return True
        p = re.compile('^[A-Z]+$')
        m = p.match(word)
        if m: 
            print(m.group())
            print("A-Z")
            return True

        p = re.compile("^[A-Z][a-z]*$")
        m = p.match(word)
        if m:
            print(m.group())
            return True

        return False

if __name__ == "__main__":
    s = Solution()

    string = "USA"
    print(s.detectCapitalUse(string))

    string = "lasdfa" 
    print(s.detectCapitalUse(string))
