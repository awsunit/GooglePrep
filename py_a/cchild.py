
from string import ascii_uppercase
from collections import Counter

def commonChild(s1,s2):
    # do the set thing
    largest = 0
    s1_set = [[]]

    for c in s1:
        for l in s:
            l += c
        s1_set += s

    s2_set = [[]]


    return largest

    # largest = 0

    # # gather location of letters
    # s1_loc = {c:[] for c in ascii_uppercase}
    # s2_loc = {c:[] for c in ascii_uppercase}

    # i = 0
    # for c in s1:
    #     s1_loc[c].append(i)
    #     i += 1

    # i = 0
    # for c in s2:
    #     s2_loc[c].append(i)
    #     i += 1

    # # filter out the non-overlapping chars
    # s2f = list(filter(lambda c: len(s1_loc[c]) > 0, s2))
    # s1f = list(filter(lambda c: len(s2_loc[c]) > 0, s1))

    # s1l = 0
    # s2l = 0

    # while s1l < len(s1f) and s2l < len(s2f):
    #     c2 = s2f[s2l]
    #     c1 = s1f[s1l]
    #     if c1 == c2:
    #         largest += 1
    #     else:
    #         in1 = s1_loc[c2]
    #         in2 = s2_loc[c1]

    #         nospots = True
    #         in1_spot = 0
            

    #         for spot in in1:
    #             # location of c2 inside s1f
    #             if spot > s1l:
    #                 in1_spot = spot
    #                 nospots = False
    #                 break

    #         if not nospots:
    #             nospots = True
    #             in2_spot = 0
    #             for spot in in2:
    #                 if spot > s2l:
    #                     in2_spot = spot
    #                     nospots = False
    #                     break
                
    #             if not nospots:
    #                 # which offers the better solution
    #                 dist1 = in1_spot - s1l
    #                 dist2 = in2_spot - s2l

    #                 if dist1 > dist2:
    #                     # we should use the char from s1
    #                     s2l = in2_spot
    #                 else:
    #                     # use the char from s2
    #                     s1l = in1_spot
                    
    #                 largest += 1


    #     s1l += 1
    #     s2l += 1

    # return largest



if __name__ == "__main__":
    s1 = "SHINCHAN"
    s2 = "NOHARAAA"
    # s1 = 'ABCDEF'
    # s2 = 'FBDAMN'
    # s1 = 'WABD'
    # s2 = 'ABDW'
    # s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
    # s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'

    # s1 = 'NWEAD'
    # s2 = 'NEADW'
    # s1 = 'HARRY'
    # s2 = 'SALLY'
    # s1 = 'AA'
    # s2 = 'BB'
    

    i = commonChild(s1,s2)

    print(i)


        # count = 0

    # # get map of locations for each char
    # counts = {c:[] for c in ascii_uppercase}
    # # print(counts)
    # spot = 0
    # for c in s2:
    #     # print(c)
    #     counts[c] += [spot]
    #     spot += 1

    # print(counts)

    # largest = 0

    # for c1 in range(len(s1)):
    #     left = 0
    #     c = 0

    #     for c2 in range(c1, len(s1)):

    #         cur_char = s1[c2]
    #         # does s2 even have this letter
    #         if counts[cur_char]:
    #             l = counts[cur_char]
    #             # is the letter located in the right spot
    #             for i in l:
    #                 if i >= left:
    #                     left = i + 1
    #                     c += 1
    #                     # dont overcount
    #                     break
    #     if c > largest:
    #         largest = c

    # return largest