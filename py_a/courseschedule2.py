'''
    course schedule II

    given courses and their pre-req's, in the form of:

    [a,b] where b is a prereq for 

    return an ordering (not unique) of courses to complete all courses

    else: []
'''

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # incoming vertices
        visited = 0

        # incoming vertices for each course -> default init to 0
        counts = {i:0 for i in range(numCourses)}
        # counts = dict.fromkeys(pre_children, 0)

        # maps course -> prereq children
        pre_children = {i:set() for i in range(numCourses)}

        # fill the map
        for l in prerequisites:
            course = l[0]
            pr = l[1]
            pre_children[pr].add(course)

        # increase our counts
        for prereq, children in pre_children.items():
            if children:
                for c in children:
                    counts[c] += 1
  
        queue = []
        order = []

        # initialize queue with any starting nodes
        for k,v in counts.items():
            if v == 0:
                print("appending: ", k)
                queue.append(k)
                

        while queue:
            n = queue.pop()
            visited += 1
            order.append(n)
            # decrease degree by one for all neighbors??
            kids = pre_children[n]
            for k in kids:
                counts[k] -= 1
                if counts[k] == 0:
                    queue.append(k)
                elif counts[k] < 0:
                    print("how would we get here")
                    return []

        print("visted == numCourses - ", visited == numCourses)
        if len(order) != numCourses:
            return []

        return order



if __name__ == "__main__":
    print("here we go")
    s = Solution()

    count = 4
    # l = [[1,0]]
    # l = [[1,0],[0,2],[2,1]] # bad
    # l = [[1,0],[1,2],[2,1],[2,0]] # bad
    l = [[1,0],[2,0],[3,1],[3,2]]
    # l = []
    o = s.findOrder(count, l)

    [print(s) for s in o]

    # stack = [1,2,3,4,5]

    # while stack:
    #     print(stack.pop())
    # print("done")
