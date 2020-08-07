from collections import Counter
def bracket_match(bracket_string):

    c = Counter(bracket_string)
    v = list(c.values())
    if len(v) < 2:
        return v[0]
    return abs(v[0] - v[1])
    # left = 0
    # right = 0
    # for i in range(len(bracket_string)):
    #     if bracket_string[i] == '(':
    #         left += 1

    #     else:
    #         right += 1

    # return abs(left - right)


if __name__ == "__main__":
    s = "(()())"
    # s = "((())"
    # s = "())"
    print(bracket_match(s))