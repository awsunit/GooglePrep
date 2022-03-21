# You are an event organizer at a university, 
# and n companies would like to do a presentation about their company at your university on Career Day. 

# However, each company have a tight schedule as to when they can come and present and how long they will present. 

# For the ith company, starting from 0, they can present starting from minute starts[i] and 
# they can present for durations[i] minutes. 

# To give every student a chance to listen to every presentation, the University can allow only one company to present at a time.

# You would like to host as many presentations as possible, so given each company's schedule, 
# find the maximum number of presentations that the university can hold.

# Parameters


#     starts: A list of integers with size n representing each company's starting time.
#     durations: A list of integers with size n representing the duration of the presentation for each company.

# Result

#     The maximum number of presentations that the university can hold.

# Examples
# Example 1:

# Input:

# starts = [1, 3, 3, 5, 7]

# durations = [2, 2, 1, 2, 1]

# Output: 4

# Explanation: Company 0 will present from minute 1~3, 
# either company 1 present from minute 3~5 or company 2 present from minute 3~4. 
# Then. company 3 and 4 can present without conflict. Therefore, a total of 4 companies can present.

from typing import List
import heapq

def max_presentations(starts: List[int], durations: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    # aux = sorted(list(zip(starts, durations)),key=lambda p: (sum(p), p[1]))
    # print(aux)

    # ans, end = 0, -float('inf')

    # for arr, dur in aux:
    #     if arr >= end:
    #         ans, end = ans + 1, arr + dur

    # return ans

    # drop = 0
    # merged = []
    # for i, time in enumerate(starts):
    #     merged.append([time, time + durations[i]])

    # merged.sort(key=lambda p: p[1])

    # print(merged)

    # cur_time = -1

    # for i in range(len(starts)):
    #     current = merged[i]
    #     if (current[0] < cur_time):
    #         print('dropping\ncurrent time, checking against: ', cur_time, current[0])
    #         drop += 1
    #     else:
    #         cur_time = current[1]

    # print('len, drop', len(starts), drop)
    # return len(starts) - drop

    # (start_time, end_time)
    aux = sorted(list(zip(starts,durations)), key=lambda p: (p[0], sum(p)))


    queue = []
    heapq.heapify(queue)

    number_of_rooms = 0

    for start, end in aux:
        print('start/end: ', start, end)
        if len(queue) == 0:
            print('queue empty')
            number_of_rooms +=1
            heapq.heappush(queue, end)
        else:
            print('queue[0]', queue[0])
            # we start after another in a room finishes
            if start >= queue[0]:
                #  don't need to create a new room
                print('using existing room')
                heapq.heappop(queue)
            else:
                print('adding room')
                number_of_rooms += 1
            heapq.heappush(queue, end)
        print('\n')

    return number_of_rooms





if __name__ == '__main__':
    starts = [int(x) for x in input().split()]
    durations = [int(x) for x in input().split()]
    res = max_presentations(starts, durations)
    print(res)