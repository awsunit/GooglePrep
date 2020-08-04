# You are given two non-empty linked lists representing 
# two non-negative integers. 

# The digits are stored in reverse order and each of their nodes
# contain a single digit. 

# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:     
        remainder = 0
        front = None
        start = None

        while l1 and l2:
            t = l1.val + l2.val + remainder
            remainder = 1 if t > 9 else 0
            temp = t - 10 if t > 9 else t

            if not start:
                # begin the list
                start = ListNode(temp)
                front = start
            else:
                start.next = ListNode(temp)
                start = start.next
                
            l1 = l1.next
            l2 = l2.next

        while l1:
            t = remainder + l1.val
            remainder = 1 if t > 9 else 0
            temp = t - 10 if t > 9 else t
            start.next = ListNode(temp)
            start = start.next
            l1 = l1.next


        while l2:
            t = remainder + l2.val
            remainder = 1 if t > 9 else 0
            temp = t - 10 if t > 9 else t
            start.next = ListNode(temp)
            start = start.next
            l2 = l2.next
        
        if remainder == 1:
            start.next = ListNode(1)

        return front