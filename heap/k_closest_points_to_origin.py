import heapq
# using negatives to make it act like a max heap
# evwn though its using min heap

def k_closest(points, k):
    heap = []
    for i in range(len(points)):
        x, y = points[i]
        distance = x * x + y * y

        if len(heap) < k:
            # add any points up to k
            # length
            heapq.heappush(heap, (-distance, i))
        elif distance < -heap[0][0]:
            # replace current furthest with a closer point
            heapq.heappushpop(heap, (-distance, i))
    
    return [points[p[1]] for p in heap]