
# import numpy as np
from collections import Counter

f = open("t_buildingpalindromes.txt", "r")

# T = int(input())
T = int(f.readline())
# print(T)

for testcase in range(1, T + 1):

    # N, Q = [int(s) for s in input().split(" ")]
    N, Q = [int(s) for s in f.readline().split(" ")]
    # print(N," ", Q)
    # get the list
    # letters = [letter for letter in input()]
    letters = [letter for letter in f.readline()]
    letters.remove('\n')

    

    # print("letters")
    # print(letters)

    canform = 0

    for q in range(1, Q + 1):
        # L, R = [int(s) for s in input().split(" ")]
        L, R = [int(s) for s in f.readline().split(" ")]

        subletters = letters[L - 1:R]
        counts = Counter(subletters)

        remaining = (R - L) + 1
        # print("remaining: ", remaining)
        mod1 = 0
        for count in counts:
            mod1 += 1 if counts[count] % 2 != 0 else 0
               
        canform += 1 if mod1 < 2 else 0
       

    print("Case #{}: {}".format(testcase, canform))




#  add = True
#         while (remaining >= 2):
#             found = False
#             amount = 2
#             for letter in counts:
#                 if counts[letter] >= amount:
#                     t = counts[letter]
#                     counts[letter] = t - amount
#                     found = True
#                     remaining -= amount
#                     # print("counts: ", counts[letter])
#                     break
#             if not found:
#                 add = False
#                 break
        
#         if add:
#             found = False
#             amount = 1
#             for letter in counts:
#                 if counts[letter] >= amount:
#                     t = counts[letter]
#                     counts[letter] = t - amount
#                     found = True
#                     remaining -= amount
#                     # print("counts: ", counts[letter])
#                     break
#             if found or remaining == 0:
#                 # print("subletters: ")
#                 # print(subletters)
#                 canform += 1


# for testcase in range(1, T + 1):

#     N, Q = [int(s) for s in input().split(" ")]
#     # N, Q = [int(s) for s in f.readline().split(" ")]
#     # print(N," ", Q)
#     # get the list
#     letters = [letter for letter in input()]
#     # letters = [letter for letter in f.readline()]
#     # letters.remove('\n')

#     # print("letters")
#     # print(letters)

#     canform = 0

#     for q in range(1, Q + 1):
#         L, R = [int(s) for s in input().split(" ")]
#         # L, R = [int(s) for s in f.readline().split(" ")]

#         subletters = letters[L - 1:R]


#         lmarker = 0
#         rmarker = R - L
#         ok = True
#         while lmarker < rmarker:
#             # print("here")
#             if subletters[lmarker] != subletters[rmarker]:
#                 # maybe another spot has a letter
#                 tr = rmarker - 1
#                 found = False
#                 while (lmarker < tr):
#                     if subletters[lmarker] == subletters[tr]:
#                         # swap right
#                         temp = subletters[tr]
#                         subletters[tr] = subletters[rmarker]
#                         subletters[rmarker] = temp
#                         found = True
#                         break
#                     if subletters[rmarker] == subletters[tr]:
#                         # swap left
#                         temp = subletters[tr]
#                         subletters[tr] = subletters[lmarker]
#                         subletters[lmarker] = temp
#                         found = True
#                         break
#                     tr -= 1

#                 if not found:
#                     ok = False
#                     break

#             lmarker += 1
#             rmarker -= 1
#         if ok:
#             # print("subletters: ")
#             # print(subletters)
#             canform += 1

# from collections import Counter
# temp = ['A','B', 'C', 'A', 'C', 'C']
# l = Counter(temp)

# for i in l:
#     print(i,l[i])

