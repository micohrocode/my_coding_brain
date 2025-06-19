from heapq import heappush, heappop

def mergeKLists(lists):
    if not lists:
        return None
    
    heap = []
    for i, node in enumerate(lists):
        if node:
            # add the first of each list to
            # the min heap
            heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    curr = dummy

    while heap:
        # take the root (smallest)
        val, idx, node = heappop(heap)
        # add to merged list
        curr.next = node
        curr = curr.next

        # if there is more in that list
        if node.next:
            # add it to the min heap
            heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next
