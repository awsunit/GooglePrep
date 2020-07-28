from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        l = [[0]]

        lastnode = len(graph) - 1

        while True:
            change = False
            rl = []
            for lst in l:
                le = lst[len(lst)-1]
                if le > lastnode:
                    
                    continue

                

                children = graph[le]
                for c in children:
                    nl = lst + [c]
                    rl += [nl]
                    change = True
                if not children:
                    rl += [lst]

            if not change:
                break
            else:

                l = rl
        
        return l




if __name__ == "__main__":
    l = [[4,3,1],[3,2,4],[3],[4],[]]

    # t = [[4]]

    # l += t
    # print(l)

    s = Solution()
    l = s.allPathsSourceTarget(l)

    print(l)