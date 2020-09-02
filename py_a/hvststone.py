import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # mis en place -> sort list
        hp = []
        for stone in stones:
            # print(stone)
            heapq.heappush(hp, -stone)
        # heapq._heapify_max(hp)
        while len(hp) > 1:
            u = heapq.heappop(hp)
            pu = heapq.heappop(hp)
            print(u, pu)
            heapq.heappush(hp,u - pu)

        return -hp[0]
            
        
if __name__ == "__main__":
    s = Solution()
    l = [2,7,4,1,8,1]
    print(s.lastStoneWeight(l))