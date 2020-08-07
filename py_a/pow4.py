class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        if num == 1:
            return True
        by2 = log(num, 2)
        # odd powers of two ! powers of four
        return by2 % 2 == 0