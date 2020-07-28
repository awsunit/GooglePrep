'''
Consider a list (list = []). 

You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  N 
followed by  lines of commands where each command will be of the 
7 types listed above. 

Iterate through each command in order and perform the 
corresponding operation on your list.

'''
def try_remove(l, v):
    try:
        l.remove(v)
    except (ValueError):
        print("not included")
        return



if __name__ == "__main__":

    # l = [1,2,3]
    # d = {"a": lambda v : try_remove(l, v)}

    # print(d["a"](5))


    # print("give us the number of commands")

    # f = open("t_convert.txt", 'r')

    # num_ops = int(f.readline())
    # print("{} commands".format(num_ops))

    num_ops = int(input())



    l = []
    operators = {"insert": lambda i,v: l.insert(i,int(v)), 
                 "print": lambda : print(l),
                 "remove": lambda v : try_remove(l, int(v)),
                 "append": lambda v: l.append(int(v)),
                 "sort": l.sort,
                 "pop": lambda: l.pop(), 
                 "reverse": lambda: l.reverse()}

    need_v = set(["insert", "remove", "append"])

    while num_ops > 0:
        # commandlist = [s for s in f.readline().split(" ")]
        commandlist = input().split()  # list command and val 
        
        
        
        command = commandlist[0].strip('\n')

        # print("looking at command: {}".format(command))

        if command in need_v:
            if command == "insert":
                operators[command](int(commandlist[1]), int(commandlist[2]))
            else:
                operators[command](commandlist[1])
        else:
            operators[command]()
        num_ops -= 1

