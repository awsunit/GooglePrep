import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    r = True

    note_counts = {}
    mag_counts = {}

    for w in magazine:
        if mag_counts.get(w):
            mag_counts[w] += 1
        else:
            mag_counts[w] = 1

    for w in note:
        if note_counts.get(w):
            note_counts[w] += 1
        else:
            note_counts[w] = 1

    for k in note_counts:
        if not mag_counts.get(k):
            r = False
            break
        if mag_counts[k] < note_counts[k]:
            r = False
            break

    if r:
        print("Yes")
    else:
        print("No")
    

if __name__ == '__main__':
    # mn = input().split()

    f = open('t_ransomnote.txt', 'r')
    mn = f.readline().split()

    m = int(mn[0])

    n = int(mn[1])

    # magazine = input().rstrip().split()
    magazine = f.readline().rstrip().split()
    note = f.readline().rstrip().split()

    # note = input().rstrip().split()

    checkMagazine(magazine, note)
    
