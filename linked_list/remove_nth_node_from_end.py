class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast,slow = dummy, dummy

    # move fast starting space over n spaces
    for _ in range(n):
        fast = fast.next
    
    # move past the node to be removed
    while fast.next:
        fast = fast.next
        slow = slow.next

    # remove the node
    slow.next = slow.next.next

    return dummy.next