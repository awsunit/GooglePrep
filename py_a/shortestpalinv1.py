class Solution:
    def shortestPalindrome(self, s: str) -> str:

        start = 0
        end = len(s) - 1
        i = 0 # start at front
        longest = (0, 0)
        while start < end:
            palin = True
            start_i = start
            end_i = end
            while start_i < end_i:
                if s[start_i] != s[end_i]:
                    palin = False
                    break
                end_i -= 1
                start_i += 1
            if palin:
                if end + 1 - start > longest[0]:
                    longest = (end + 1 - start, end)
                
            end -= 1

        # if here, than singleton case?
        return self.make_me(longest[1] + 1, s)

    def make_me(self, end, s):
        # after end needs to be appended
        sb = s[end:]
        sb = sb[::-1]
        return sb + s

if __name__ == "__main__":
    # s = "aacecaaa"
    # s = "abcd"
    # s = "aabba"
    # s = "s"
    # s = "aabba"
    print(Solution().shortestPalindrome(s))