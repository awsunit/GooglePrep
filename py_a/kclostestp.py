# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # want a map : dist -> point
        # priority queue
        dq = []
        m = {}

        # built-in -> sqrt
        for p in points:
            d = sqrt(pow(p[0],2) + pow(p[1],2))
            m[d] = p

        for distances in m.keys():
            heapq.heappush(distances)

        l = []
        while (K > 0):
            l.append(m[heapq.heappop(dq)])
            K -= 1

        return l

if __name__ == "__main__":
    l = [[1,3],[-2,2]]
    s = Solution()
    print(s.kClosest(l,1))
