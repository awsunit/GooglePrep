from string import ascii_lowercase
import os
from collections import Counter
import string


def recurse(currentSpot, lengthOfWord, word, letters):
    print('here:\n', currentSpot, lengthOfWord, word, letters)

    if currentSpot == lengthOfWord:
        # any errors would have been reported already
        return 1

    siblingSpot = lengthOfWord - currentSpot - 1
    wordsCurrentLetter = word[currentSpot]
    filteredLetters = list(filter(lambda letter: letter <= wordsCurrentLetter, letters))
    print(filteredLetters)

    length = len(filteredLetters)

    if length == 0:
        return 0

    

    if siblingSpot == currentSpot or siblingSpot == currentSpot + 1:
        print('middle letter or palin of two, {}'.format(length))
        # string of length one is a palindrone
        # string of length two can only be a palindrone iff both letters are the same
        filteredLetters = filter(lambda: letter, letter <filteredLetters)
        return length
    # elif siblingSpot == currentSpot + 1:
    #     print('palindrones of two letters, {}'.format(length))
    #     # string of length two can only be a palindrone iff both letters are the same
    #     # need to check if palindrones would have lower cardinality 
    #     return length
    else:
        print('checking the rest')
        # return letters.length * recurse(currentSpot + 1, lengthOfWord, word, letters)
        return length * recurse(currentSpot + 1, lengthOfWord, word, letters)
    # through combinatorics?
    # every spot has letters.length of options
    # a, b, c
    # _ _ _
    # first and last spot has 3 options:
    # a_a, b_b, c_c 

    # a, b, c
    # _ _ _ _ _
    # a _ _ _ a, b _ _ _ b, c _ _ _ c


def howMany(f):
    # length of string, how many letters in the alphabet
    # word = f.readline().rstrip()
    N, K = [int(s) for s in input().split(" ")]
    word = input().rstrip()
    letters = [s for s in ascii_lowercase[0:K]]
    currentLetter = 0

    return recurse(currentLetter, N, word, letters)


def solve(f):
    print(f)

    # testcases = int(f.readline().rstrip())
    testcases = int(input().rstrip())

    for testcase in range(testcases):

        numPalindromes = howMany(f)
        print("Case #{}: {}".format(testcase + 1, numPalindromes))




if __name__ == '__main__':
    # fptr = open('./test/smallerstrings.txt', 'r')
    # solve(fptr)
    a = 's'
    solve(a)
