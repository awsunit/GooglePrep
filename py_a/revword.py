class Solution:
    def reverseWords(self, s: str) -> str:
        # split into array, remove white space
        # reverse with a space between each word
        print(s)

        nowh = " ".join(s.split())

        spl = nowh.split(" ")
        spl = spl[::-1]
        [print(v) for v in spl]

        s = " ".join(spl)
        # # s = s.replace(" ", "", 1)
            
        print(s + '\n')
        return s


if __name__ == "__main__":
    s = Solution()
    v = " hello world! "
    # s.reverseWords(v)
    s.reverseWords(" a good  example ")