# Let S be a string containing only letters of the English alphabet. 

# An anagram of S is any string that contains exactly the same letters as S (with the same number of occurrences for each letter), but in a different order. 

# For example, the word kick has anagrams such as kcik and ckki.

# Now, let S[i]
# be the i-th letter in S. We say that an anagram of S, A, is shuffled if and only if for all i, S[i]≠A[i]. So, for instance, 

# kcik is not a shuffled anagram of kick as the first and fourth letters of both of them are the same. 
# However, ckki would be considered a shuffled anagram of kick, as would ikkc.

# Given an arbitrary string S, output any one shuffled anagram of S or else print IMPOSSIBLE if this cannot be done.

# Input

# The first line of the input gives the number of test cases, T. 

# T test cases follow. 

# Each test case consists of one line, a string of English letters.

# Output

# For each test case, output one line containing 
# Case #x: y, where x is the test case number (starting from 1) and y is a shuffled anagram of the string for that test case, 
# or IMPOSSIBLE if no shuffled anagram exists for that string. 

from collections import Counter

def recurse(word, currentSpot, numOccurences, anagram):
    if currentSpot == len(word):
        return anagram

    wordsLetter = word[currentSpot]
    for k,v in numOccurences.items():
        if k != wordsLetter and v > 0:
            copy = numOccurences.copy()
            copy[k] -= 1
            result = recurse(word, currentSpot + 1, copy, anagram + k)
            if result != 'IMPOSSIBLE':
                return result
            
    
    return 'IMPOSSIBLE'

def solve(testcases):
    for testcase in range(testcases):
        word = input().rstrip()
        numOccurrences = Counter(word)
        anagram = recurse(word, 0, numOccurrences, '')
        print("Case #{}: {}".format(testcase + 1, anagram))




if __name__ == '__main__':
    # fptr = open('./test/smallerstrings.txt', 'r')
    # solve(fptr)
     # testcases = int(f.readline().rstrip())
    testcases = int(input().rstrip())
    solve(testcases)
