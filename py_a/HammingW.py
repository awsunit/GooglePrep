# Write a function that takes an unsigned integer and 
# return the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:

        i = 0
        count = 0
        # if n & 1:
        #     count += 1
        while i < 32:
            if n & (1 << i):
                count += 1
            i += 1

        return count


if __name__ == "__main__":
    s = Solution()

    print(s.hammingWeight(11))
    print(s.hammingWeight(128))