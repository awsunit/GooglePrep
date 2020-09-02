# You are given two non-empty linked lists representing two non-negative integers. 

# The most significant digit comes first and each of their nodes contain a single digit. 

# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Problems discovered:
# python list was not pass by reference -> lots of copies being made
# we need to get better
# if the data is "skewy" fucking fix it!

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def fix(self, l1, l2):
        t1 = l1.next
        t2 = l2.next
        t1c = 1
        t2c = 1
        while (t1 is not None):
            t1c += 1
            t1 = t1.next
        while t2 is not None:
            t2c += 1
            t2 = t2.next
        if (t1c != t2c):
            diff = abs(t1c - t2c)
            if t1c < t2c:
                l1 = self.smaller(l1, diff)
            else:
                l2 = self.smaller(l2, diff)
        # self.printlist(l1)
        # self.printlist(l2)
        return l1, l2

    def printlist(self, LN):
        while (LN is not None):
            print(LN.val)
            LN = LN.next
        # print("pl")

    def smaller(self, l, diff):
        smaller = l
        while (diff > 0):
            l = ListNode(val=0, next=smaller)
            smaller = l
            diff -= 1
        return smaller

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.fix(l1, l2)
        # self.printlist(l1)
        # self.printlist(l2)
        n, c = self.recurse(l1, l2)
        return n

    def recurse(self, l1, l2):
        # base
        if l1 is None and l2 is None:
            return (None, 0)

        # add, get the remainder
        (l, carry) = self.recurse(l1.next, l2.next)
        v = l1.val + l2.val + carry
        c = 0
        if v > 9:
            v = v - 10
            c = 1
        us = ListNode(val=v, next=l)
        return (us, c)

if __name__ == "__main__":
    l1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1))))
    l2 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1)))

    s = Solution()
    ln = s.addTwoNumbers(l1, l2)
    while ln is not None:
        print(ln.val)
        ln = ln.next



      