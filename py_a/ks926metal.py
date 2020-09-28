# You are in charge of deploying robots to harvest Kickium 
# from a nearby asteroid. 

# Robots are not designed to work as a team, 
# so only one robot can harvest at any point of time. 

# A single robot can be deployed for up to K units of time 
# in a row before it returns for calibration, 
# regardless of how much time it spends on harvesting during that period. 

# Harvesting can only be done during specific time intervals. 
# These time intervals do not overlap. 

# Given K and the time intervals in which harvesting is allowed, 
# what is the minimum number of robot deployments required to 
# harvest at all possible times?

import math

def solve(testcases):

    for testcase in range(testcases):
        # num pairs, max time per robot
        N, K = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case

        htimes = []
        for n in range(N):
            s, e = [int(s) for s in input().split(" ")] 
            htimes.append((s, e))  

        # sort our list by the start
        ht = sorted(htimes, key=lambda tup: tup[0])

        robots = 0
        lo = 0
        # the amount of time which has passed
        last_e = 0
        # K is max time per robot
        for s_i, e_i in ht:
            # some robot was working for some amount
            # of leftover time
            lo = max(0, lo - (s_i - last_e))
            # change over
            last_e = e_i

            duration = e_i - s_i
            if lo > duration:
                lo -= duration
                # anything else
            else:
                duration -= lo
                # how many robots
                deploy = math.ceil(duration/K)
                robots += deploy
                lo = (K*deploy) - duration

        print("Case #{}: {}".format(testcase + 1, robots))


t = int(input())
solve(t)