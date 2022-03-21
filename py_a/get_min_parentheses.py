



#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMin(s):
    # Write your code here
    min_parenthese = 0

    stack = []

    for parenthese in s:
        if parenthese == ')':
            if len(stack) == 0:
                min_parenthese += 1
            else:
                stack.pop()
        else:
            stack.append(parenthese)
     
    return min_parenthese + len(stack)

if __name__ == '__main__':

    s = input()

    result = getMin(s)

    print(result)