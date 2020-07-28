
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print("addBinary")
        "pad out smaller string with 0's"
        if len(a) > len(b):
            diff = len(a) - len(b)
            while diff > 0:
                b = "0" + b
                diff -= 1
        if len(b) > len(a):
            diff = len(b) - len(a)
            while diff > 0:
                a = "0" + a
                diff -= 1

        print(a, b)
        return self.abi(a,b,"0","")


    def abi(self, a, b, carry, result):
        if a == "" or b == "":
            if carry == "1":
                return carry+a+b+result
            return a+b+result

        # add numbers
        sa = a[0:len(a) - 1]
        sb = b[0:len(b) -1 ]

        aa = a[-1]
        bb = b[-1]

        print("sa: {}\nsb: {}\naa: {}\nbb: {}".format(sa, sb, aa, bb))
        val = ""
        if aa == "1" and bb == "1":
            if carry == "1":
                val = "1"
            else:
                val = "0"
            carry = "1"
        elif aa == "1" or bb == "1":
            if carry == "1":
                val = "0"
                # leave carry alone
            else:
                val = "1"
                # leave carry alone
        else:
            # all zeroes
            val = carry
            carry = "0"
        result = val + result
        print("result: ",result)
        return self.abi(sa, sb, carry, result)
        # carry

if __name__ == "__main__":
    print(len("h"))

    s = Solution()
    a = "1010"
    b = "1011"
    
    print(s.addBinary(a, b))