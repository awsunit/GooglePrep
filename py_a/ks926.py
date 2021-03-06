# There are N people numbered from 1 to N, 
# standing in a queue to withdraw money from an ATM. 

# The queue is formed in ascending order of their number. 
# The person numbered i wants to withdraw amount Ai. 
# The maximum amount a person can withdraw at a time is X. 

# If they need more money than X, they need to go stand at the 
# end of the queue and wait for their turn in line. 

# A person leaves the queue once they have withdrawn 
# the required amount.

# You need to find the order in which all the people leave the queue.

import math

def solve(testcases):

    for testcase in range(testcases):
        N, X = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
        
        
        wd = [int(s) for s in input().split(" ")]
        wdm = [(x + 1, math.ceil(wd[x]/X)) for x in range(len(wd))]

        wd = sorted(wdm, key=lambda tup: tup[1])
        order = [p for p, times in wd]

        print("Case #{}: {}".format(testcase + 1," ".join(str(i) for i in order)))

t = int(input())
solve(t)
