'''
    Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return self.nwb(numBottles, numExchange, 0, 0)

    def nwb(self, numBottles, numExchange, empties, count):

        while (numBottles > 0):
            count += numBottles
            empties += numBottles
            numBottles = int(empties/numExchange)
            empties = empties % numExchange

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numWaterBottles(5, 5))
    print(s.numWaterBottles(2,3))
    print(s.numWaterBottles(15,4))