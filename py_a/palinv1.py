import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ns = re.sub(r"[^a-z0-9]| ", "", s)

        start = 0
        end = len(ns) - 1
        while start < end:
            if ns[start] != ns[end]:
                return False
            start += 1
            end -= 1

        return True

            

if __name__ == "__main__":
    
    s = "this Is &as I jpp s ,."
    s = s.lower()
    ns = re.sub(r"[^a-z]| ", "", s)
    print(Solution().isPalindrome("0P"))