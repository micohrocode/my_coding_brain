class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    tail, first = dummy, head

    while first and first.next:
        second = first.next

        # swap the nodes
        tail.next = second
        first.next = second.next
        second.next = first

        # move the tail over to the newly swapped node
        tail = first

        # move to the next node
        first = first.next

    return dummy.next