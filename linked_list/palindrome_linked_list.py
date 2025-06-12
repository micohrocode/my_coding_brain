class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # starting at the middle of the list
    curr, prev = slow, None
    while curr:
        # reverse the second half of the list
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    # start at both ends
    left, right = head, prev
    while right:
        # check if its not a palindrome
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True