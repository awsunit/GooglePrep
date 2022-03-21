def segment(x, space):
    # Write your code here
    
    min_disk = []
    space_len = len(space)
    
    for index,computer in enumerate(space):
        #  starting at 0
        # want 2
        #  0 + 2 = 2
        range_end = index + x
        if range_end <= space_len:
            print('looking at ranges: ', index, range_end)
            # we can run the test
            # start with first item as min
            min_val = computer
            for next_computer in range(index + 1, range_end):
                if space[next_computer] < min_val:
                    print('new min', space[next_computer])
                    min_val = space[next_computer]
            min_disk.append(min_val)
        
    
    return max(min_disk)

if __name__ == '__main__':

    x = int(input().strip())

    space = [int(x) for x in input().split()]

    print('space, x: ', space, x)

    result = segment(x, space)
    print(result)