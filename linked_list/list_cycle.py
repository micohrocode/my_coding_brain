class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        # move each pointer
        slow = slow.next
        fast = fast.next.next

        # if they eventually equal each other
        # before there is nothing for fast to point to
        # then there is a cycle
        if slow == fast:
            return True
    
    return False