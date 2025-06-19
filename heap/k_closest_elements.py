import heapq

def k_closest(nums, k, target):
    heap = []

    for num in nums:
        # calc distance to target
        distance = abs(num - target)

        if len(heap) < k:
            # fill until length reached
            heapq.heappush(heap, (-distance, num))
        elif distance < -heap[0][0]:
            # replace furtheset with one that is closer
            # if a closer one is found
            heapq.heappush(heap, (distance, num))
    
    distances = [pair[1] for pair in heap]
    distances.sort()
    return distances