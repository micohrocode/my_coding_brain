import heapq

def kth_largest(nums, k):
    if not nums:
        return
    
    heap = []

    for num in nums:
        if len(heap)<k:
            # fill the heap only until 
            # it meets k length
            heapq.heappush(heap, num)
        elif num > heap[0]:
            # then only replace the lowest node
            # if a higher one appears
            heapq.heappushpop(heap, num)
    
    return heap[0]
    