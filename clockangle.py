class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hourangle = (.5*minutes) if hour == 12 else (hour * 30) + (.5*minutes)
        minangle = minutes * 6

        v1 = abs(hourangle - minangle)
        v1 = v1 if v1 < 180.0 else 360.0 - v1
        return v1

if __name__ == "__main__":
    a = 1
    b = 57
    s = Solution()
    print(s.angleClock(a, b))