class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return head
    
    # find the middle of the list
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_ = curr.next
        curr.mext = prev
        prev, curr = curr, next_

    # merge the lists
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head