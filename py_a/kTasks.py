

from typing import List

def game(p: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    totals = []

    runningSum = 0
    totals = [] 
    for probability in p:
        numToAdd = 1 if probability == 1 else -1
        runningSum += numToAdd
        print('runningSum: ', runningSum)
        totals.append(runningSum)

    maxScore = max(totals)
    print('maxScore: ', maxScore)

    finalTotal = totals[len(totals) - 1]
    
    if 0 > finalTotal:
        return 0

    for count, total in enumerate(totals):
        # edge case where we may not be the largest score but we will beat the final score

        nMinusKTotal = finalTotal - total
        print('Total: {}, nMinusKTotal: {}'.format(total, nMinusKTotal))
        if total > nMinusKTotal:
            # add 1 since we are doing a task here
            return count + 1

    return -1

if __name__ == '__main__':
    p = [int(x) for x in input().split()]
    res = game(p)
    print(res)
