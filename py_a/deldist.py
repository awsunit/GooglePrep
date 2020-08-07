def deletion_distance(str1, str2):
    dist = 0

    shortest = str1 if len(str1) < len(str2) else str2
    longest = str2 if len(str1) <= len(str2) else str1
    spot = 0
    while spot < len(shortest):
        temp = spot
        while temp < len(shortest) and shortest[spot] != longest[temp]:
            dist += 1
            temp += 1
        # at a matching character
        spot = temp + 1

    if spot < len(longest):
        print("longer")
        dist += len(longest) - spot
    return dist

def push(value, r=[]):
    r.append(value)
    return r
if __name__ == "__main__":
    f = push(0)
    push(1, f)
    print(push(2))

