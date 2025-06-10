def nonOverlappingIntervals(intervals):
    if not intervals:
        return 0
    
    # sort intervals byt their end time
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1

    for i in range(1, len(intervals)):
        # if the interval is not overlapping
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    
    # take the total intervals - non overlapping
    return len(intervals) - count
