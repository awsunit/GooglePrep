# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        front = head

        while head is not None:
            if head.val == val:
                # print("removing")
                if prev is not None:
                    prev.next = head.next
                else:
                    front = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        
        return front

if __name__ == "__main__":
    
    # problems:
    # lost head of list
    # forgot to incremenet prev
    # ugly logic in places
    # trouble when head removed -> forgot to increment head of list
    # come on todd

    # one item linkedlist


    f = open('rlle.txt', 'r')


    lines = f.readlines()

    head = None
    cur = None
    for line in lines:
        val = int(line)

        if head == None:
            head = ListNode(val, None)
            cur = head
        else:
            n = ListNode(val, None)
            cur.next = n
            cur = n
    s = Solution()

    head = ListNode(6, None)
    h = s.removeElements(head, 6) 
    while h is not None:
        print(h.val)

