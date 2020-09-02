class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}

        # map
        for i in nums:
            if map.get(i):
                map[i] += 1
            else:
                map[i] = 1

        # itemgetter, and functions in the operator module in general, are fast
        r = sorted(map, key=map.get, reverse=True)

        return r[0:k]

if __name__ == "__main__":
    s = Solution()
    r = [1,1,1,2,2,3]
    k = 2
    v = s.topKFrequent(r, k)
    [print(i) for i in v]