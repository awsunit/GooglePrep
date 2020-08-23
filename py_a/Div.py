class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or divisor == 0:
            return 0


        ndivisor = abs(divisor)
        ndividend = abs(dividend)

        if ndivisor == 1:
            if divisor < 0 :
                return -dividend
            return dividend

        i = 0

        print(ndividend, ndivisor)
        while ndividend >= ndivisor:
            i += 1
            ndividend -= ndivisor

        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            return i
        return -i


if __name__ == "__main__":
    s = Solution()

    print(s.divide(-1, 1))
    print(s.divide(-1, -1))
    print(s.divide(-2147483648, -1))
  