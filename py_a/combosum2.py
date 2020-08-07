
from typing import List
from itertools import chain, combinations
class Solution:

    def fc(self, candidates: List[int], index: int, target: int, cur: List[int], r: List[List[int]]) -> None:

        if target == 0:
            r.append([x for x in cur])
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            if i == index or candidates[i] != candidates[i-1]:
            # if i == 0 or candidates[i] != candidates[i-1]:
                cur.append(candidates[i])
                self.fc(candidates, i + 1, target - candidates[i], cur, r)
                cur.pop(len(cur) - 1)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        l = sorted(candidates)

        self.fc(l, 0, target, [], r)
        return r
        
        # works but is slowwwww
        # r = []
        # sbsets = ()
        # # generate all subsets w/ lists
        # r = []
        # sbsets = list(chain.from_iterable(combinations(candidates, r) for r in range(len(candidates) + 1)))
        # print(sbsets)
        # # sbsets = []
        
        # # for l in candidates:
        # #     a = [sb + [l] for sb in sbsets]
        # #     # print("a: " , a)
        # #     # print("sbsets: ", sbsets)
        # #     for ai in a:
        # #         sbsets.append(ai)
        # #     sbsets.append([l])
        #     # print(sbsets)
        # s = list(filter(lambda x: sum(x) == target, sbsets))
        # s1 = [sorted(x) for x in s]
        # t = ()
        # for l in s1:
        #     t += (tuple(l),)
        # s1 = set(t)
        # return s




if __name__ == "__main__":
    c = [10,1,2,7,6,1,5]
    l = 8
    print(Solution().combinationSum2(c, l))
    
