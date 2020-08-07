def longest_flat(array):
    longest = 0

    spot = 0
    while spot < len(array):
        temp = 1
        v = array[spot]
        spot += 1
        while spot < len(array) and array[spot] == v:
            temp += 1
            spot += 1
        if temp > longest:
            longest = temp

    return longest


if __name__ == "__main__":
    # l = [1,1,2,2,2]
    l = [1,1,2,2,2,2]
    l = []
    print(longest_flat(l))