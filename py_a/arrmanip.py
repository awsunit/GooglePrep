import numpy as np

# def arrayManipulation(n, queries):
#     maxi = 0
#     c = [0 for i in range(n+1)]
#     counts = np.array(c)


#     # add third betwen first, second
#     for l, r, v in queries:
#         # print(l, r)
#         sub = counts[int(l): int(r)+1]
#         # print(sub)
#         sub = sub + int(v)
#         # print(sub)
#         counts[int(l): int(r)+1] = sub
#         # for spot in sub:
#         #     counts[spot] += int(v)
#         #     print(spot, counts[spot])

#     # [print(i,c) for i,c in counts.items()]

#     return max(counts)


def arrayManipulation(n, queries):
    counts = {i:0 for i in range(n+1)}
    # counts = np.array(c)



    # add third betwen first, second
    for l, r, v in queries:
        l = int(l)
        r = int(r)
        v = int(v)
        # rng = range(l, r+1)
        # print(l, r)
        # counts = dict(map(lambda kv: (kv[0], kv[1] + v) if kv[0] in rng else kv, counts.items()))
        # print(sub)

        # print(sub)
        # counts = dict(map(lambda k: k[1]+v if k[0] in rng else k[1], counts.items()))
        for spot in range(l,r+1):
            counts[spot] += v
            # print(spot, counts[spot])

    # [print(i,c) for i,c in counts.items()]

    return max(counts.values())

if __name__ == "__main__":
    
    f = open('t_arrmanip.txt', 'r')

    out = open('lsr.txt','w')

    n, m = [int(i) for i in f.readline().split()]

    queries = []

    while m > 0:
        queries.append(f.readline().split())
        m -= 1

    r = arrayManipulation(n, queries)

    print("max number: {}".format(r))

    out.write(str(r))

    l = [i for i in range(0,11)]
    print(l)
    l = list(map(lambda a: a + 5, l))
    print(l)

    # d = {i:0 for i in range(6)}

    # print(d)
    # rng = range(2,4)


    # d = dict(map(lambda kv: (kv[0], kv[1] + 100) if kv[0] in rng else (kv[0],9), d.items()))
    # print(d)
    # d = {i:0 for i in range(6)}