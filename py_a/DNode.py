# Write a function to delete a node (except the tail) in a 
# singly linked list, given only access to that node.

# Given linked list -- head = [4,5,1,9], which looks like 
# following:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # keep changing vals until end
        prev = node

        while (node.next.next):
            node.val = node.next.val
            node = node.next
        
        node.val = node.next.val
        node.next = None
  

