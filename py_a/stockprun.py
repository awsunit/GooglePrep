def stock_runs(prices):

    if len(prices) < 2:
        return 0

    longest = 0
    spot = 0

    while spot < len(prices):
        temp = 1
        prev = prices[spot]
        nxt = spot + 1
        # check for continual growth
        while nxt < len(prices) and prices[nxt] > prev:
            prev = prices[nxt]
            nxt += 1
            temp += 1        
        if temp > longest:
            longest = temp
        
        temp = 1
        prev = prices[spot]
        nxt = spot + 1
        while nxt < len(prices) and prices[nxt] < prev:
            prev = prices[nxt]
            nxt += 1
            temp += 1        
        if temp > longest:
            longest = temp

        spot += 1

    return longest

if __name__ == "__main__":
    l = [1,2,3]
    l = [2,3,4,3,2,1]

    print(stock_runs(l))
