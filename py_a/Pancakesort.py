# 1 <= A.length <= 100
# 1 <= A[i] <= A.length
# All integers in A are unique 
# (i.e. A is a permutation of the integers from 1 to A.length).
from typing import List
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        r = []
        # get locations?? -> no
        spot = len(A)

        while spot > 0:  # 0 would be sorted?
            local = A.index(max(A[0:spot]))
    
            r.append(local)
            r.append(spot - 1)
            # print(A)
            self.flip(A, 0, local)
            # print(A)
            self.flip(A, 0, spot - 1)
            # print(A)
            spot -= 1

        return r

    def flip(self, A, start, end):
        while (start < end):
            t = A[start]
            A[start] = A[end]
            A[end] = t
            start += 1
            end -= 1

if __name__ == "__main__":
    A = [3,2,4,1]
    s = Solution()
    print(s.pancakeSort(A))
    print(A)