from typing import List
from queue import LifoQueue


def differs_by_one(word1, word2):
    # print('word1, word2: {}, {}'.format(word1, word2))
    if len(word1) != len(word2):
        return False
    alreadyOffByOne = False
    for letter in range(len(word1)):
        if word1[letter] != word2[letter]:
            if alreadyOffByOne:
                return False
            alreadyOffByOne = True
    return True

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    # what we want - is to find all the words who differ from current word by only one letter
    off_by_one = {}

    for current_i, current_word in enumerate(word_list):
        # ensure current is in map
        if current_word not in off_by_one:
            off_by_one[current_word] = {}
        for inner_i, inner_word in enumerate(word_list):
            # ensure inner is in map
            if inner_word not in off_by_one:
                off_by_one[inner_word] = {}
            if current_i != inner_i:
                # compare words
                if differs_by_one(current_word, inner_word):
                    # map us
                    off_by_one[current_word][inner_word] = True
                    off_by_one[inner_word][current_word] = True


    for key, value in off_by_one.items():
        print('key, value: {}, {}'.format(key, value))


    queue = []
    queue.append({'word': begin, 'depth': 0})
    depth = 0

    seen = []

    while len(queue) > 0:
        word_object = queue.pop(0)
        seen.append(word_object['word'])
        print('looking at word: {}, depth is: {}'.format(word_object['word'], word_object['depth']))

        sibling_words = off_by_one[word_object['word']]
        off_by_one.pop(word_object['word'])

        for sibling in sibling_words:
            if sibling == end:
                return word_object['depth'] + 1
            else:
                if sibling not in seen:
                    seen.append(sibling)
                    queue.append({'word':sibling, 'depth': word_object['depth'] + 1})
    
    # what if it cant be done?
    return depth
    

if __name__ == '__main__':
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)