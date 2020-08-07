# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

# For a given query word, the spell checker handles two categories of spelling mistakes:

# Capitalization: 
# If the query matches a word in the wordlist (case-insensitive), 
# then the query word is returned with the same case as the case in the wordlist.

# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"

# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel
# individually, it matches a word in the wordlist (case-insensitive), 
# then the query word is returned with the same case as the match in the wordlist.

# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)

# In addition, the spell checker operates under the following precedence rules:

# When the query exactly matches a word in the wordlist (case-sensitive), 
# you should return the same word back.

# When the query matches a word up to capitlization, you should return the first such match in the wordlist

# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.

# If the query has no matches in the wordlist, you should return the empty string.

# Given some queries, return a list of words answer, where answer[i] is the correct word for
#  query = queries[i].

from typing import List
import re

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # need to return the first such match...
        # map: augemented to original
        unchanged = {}
        nocapitals = {}
        novowels = {}
        r = []
        spot = 0

        # weird one
        # wordlist = wordlist[::-1]

        unchanged = {w:w for w in wordlist}

        # many->1 and we want firsties
        wordlist = wordlist[::-1]

        nocapitals = {w.lower():w for w in wordlist}

        p = re.compile("[aeiou]")
        novowels = {p.sub("*", w.lower()):w for w in wordlist}


        print(unchanged)
        print(nocapitals)
        print(novowels)
        for word in queries:
            low = word.lower()
            nword = p.sub("*", low)
            if unchanged.get(word):
                r.append(word)
            elif nocapitals.get(low):
                r.append(nocapitals[low])
            elif novowels.get(nword):
                r.append(novowels[nword])
            else:
                r.append("")

        # for word in queries:
        #     low = word.lower()
        #     nv = re.sub("[aeiou]", "", word.lower())
        #     if unchanged.get(word):
        #         r.append(word)
        #     elif capitals.get(low):
        #         r.append(capitals[low][0])
        #     else:
        #         # try to remove values
        #         # reduce
        #         for w, wi, loc in unchanged:
        #             if wi[0] == word[0]:
        #                 shortest = min(wi, word, key=len)
        #                 longest = max(wi, word, key=len)
        #                 bad = False
        #                 for i in range(len(shortest)):
        #                     if re.match("[eaiou]", shortest[i]) and not re.match("eaiou", longest[i]):
        #                         bad = True
        #                         break




        return r

        
if __name__ == "__main__":
    l = ["KiTe","kite","hare","Hare"]
    q = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    print(Solution().spellchecker(l, q))
    # shortest = "face"
    # for i in range(len(shortest)):
    #     if re.match("[fa]",shortest[i]):
    #         print("yup")