
# Implement the class ProductOfNumbers that supports two methods:

# 1. add(int num)

# Adds the number num to the back of the current list of numbers.
# 2. getProduct(int k)

# Returns the product of the last k numbers in the current list.
# You can assume that always the current list has at least k numbers.
# At any time, the product of any contiguous sequence of numbers will 
# fit into a single 32-bit integer without overflowing.
from collections import deque
class ProductOfNumbers:

    def __init__(self):
        self.deq = deque()
        

    def add(self, num: int) -> None:
        

    def getProduct(self, k: int) -> int:
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)